from django import forms


class RedirectToPortfolioForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter GitHub username',
                   'class': 'px-5 py-3 border-0 border w-100 border-0 border rounded-pill', 'style': 'font-size: 1.2rem;'}
        )
    )
