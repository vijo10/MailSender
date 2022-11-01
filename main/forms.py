from django import forms


class mailForm(forms.Form):
    to=forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control my-2",'placeholder':"Enter Email"}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control my-2",'placeholder':"Enter Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control my-2",'placeholder':"Write..."}))