from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from .config import *

from django.http import HttpResponseRedirect, JsonResponse
import requests
import calendar
from .forms import RedirectToPortfolioForm
from datetime import datetime

time_now = datetime.now()


def home(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            return redirect(reverse('about', args=[username]))
        else:
            error = 'Please enter a valid GitHub username'
            form = RedirectToPortfolioForm()
            context = {'form': form, 'error': error,
                       'site_name': SITE_NAME, 'site_url': SITE_URL}
            return render(request, 'pages/home.html', context)

    else:
        form = RedirectToPortfolioForm()
        context = {'form': form, 'site_name': SITE_NAME, 'site_url': SITE_URL}
        return render(request, 'pages/home.html', context)


def about(request, username):

    about_url = GITHUB_API_URL + '/users/' + username

    try:
        response = requests.get(about_url, headers=GITHUB_API_HEADERS)
        data = response.json()

        # Check API error message and render error page
        if 'message' in data:
            return render(request, 'handlers/_error.html', {'error': data, 'current_time': time_now.strftime("%d %B, %Y %I:%M %p"), 'site_name': SITE_NAME})

        # Convert created_at date to readable format
        years = data['created_at'][0:4]
        months = int(data['created_at'][5:7])
        days = data['created_at'][8:10]
        data['created_at'] = calendar.month_name[months] + \
            ' ' + days + ', ' + years
        data['on_github'] = time_now.year - int(years)

        context = {'user': data,  'current_time': time_now.strftime(
            "%d %B, %Y %I:%M %p"), 'site_name': SITE_NAME}
        return render(request, 'pages/about.html', context)

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return JsonResponse({'error': str(e)}, status=500)


def connections(request, username, page=1):

    about_url = GITHUB_API_URL + '/users/' + username
    followers_url = 'https://api.github.com/users/' + \
        username + '/followers?per_page=100' + '&page=' + str(page)
    followings_url = 'https://api.github.com/users/' + \
        username + '/following?per_page=100' + '&page=' + str(page)

    try:
        about_response = requests.get(about_url, headers=GITHUB_API_HEADERS)
        followers_response = requests.get(
            followers_url, headers=GITHUB_API_HEADERS)
        followings_response = requests.get(
            followings_url, headers=GITHUB_API_HEADERS)

        about_data = about_response.json()
        followers_data = followers_response.json()
        followings_data = followings_response.json()

        context = {'user': about_data, 'followers': followers_data,
                   'followings': followings_data, 'current_time': time_now.strftime("%d %B, %Y %I:%M %p")}

        return render(request, 'pages/connection.html', context)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def projects(request, username, page=1):

    about_url = GITHUB_API_URL + '/users/' + username
    repos_url = GITHUB_API_URL + '/users/' + username + '/repos?per_page=100' + \
        '&page=' + str(page) + '&sort=updated&direction=desc'

    try:
        about_response = requests.get(about_url, headers=GITHUB_API_HEADERS)
        repos_response = requests.get(repos_url, headers=GITHUB_API_HEADERS)

        about_data = about_response.json()
        repos_data = repos_response.json()

        context = {'repos': repos_data, 'current_time': time_now.strftime(
            "%d %B, %Y %I:%M %p"), 'user': about_data}

        return render(request, 'pages/project.html', context)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def cv(request, username):

    about_url = GITHUB_API_URL + '/users/' + username

    try:
        about_response = requests.get(about_url, headers=GITHUB_API_HEADERS)

        about_data = about_response.json()

        if about_data['hireable'] == False or about_data['hireable'] == None:
            error = {
                'message': "This user is not available for hire. Please check back later."}
        else:
            error = {
                'message': "CV building Failed! But, This user is available for hire. Please contact directly."}

        context = {'user': about_data, 'current_time': time_now.strftime(
            "%d %B, %Y %I:%M %p"), 'site_name': SITE_NAME, 'error': error}

        return render(request, 'handlers/_error.html', context)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def about_us(request):
    return render(request, 'about_us.html', {'site_name': SITE_NAME})
