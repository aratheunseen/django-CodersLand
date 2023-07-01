from django.urls import path
from .views import *

urlpatterns = [
    # root
    path('', home, name='home'),

    # site info pages
    path('about/', about_us, name='about us'),
    path('features/', about_us, name='features'),
    path('docs/', about_us, name='docs'),
    path('credits/', about_us, name='credits'),

    # policies pages
    # path('privacy/', privacy, name='privacy'),
    # path('terms/', terms, name='terms'),
    # path('cookies/', cookies, name='cookies'),
    # path('copyright/', copyright, name='copyright'),

    # dynamic user pages
    path('<str:username>/', about, name='about'),
    path('<str:username>/connections/', connections, name='connections'),
    path(r'<str:username>/connections/<int:page>/',
         connections, name='connections page'),
    path('<str:username>/projects/', projects, name='projects'),
    #     path('<str:username>/projects/<int:page>/', projects, name='projects page'),
    path(r'<str:username>/projects/<int:project_id>/',
         project_view, name='project view'),
    path('<str:username>/cv/', cv, name='cv'),
]
