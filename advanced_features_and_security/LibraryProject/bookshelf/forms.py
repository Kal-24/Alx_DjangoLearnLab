from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter book title'})
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter author name'})
    )
    publish_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
