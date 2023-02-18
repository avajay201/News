from django import forms

class Sign_Up_Form(forms.Form):
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    password = forms.CharField(label = 'Password', widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    email = forms.EmailField(label = 'Email Address', widget = forms.TextInput(attrs = {'class' : 'form-control'}))

class Sign_In_Form(forms.Form):
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs = {'id': 'login_username', 'class': 'form-control'}))
    password = forms.CharField(label = 'Password', widget = forms.TextInput(attrs = {'id': 'login_password', 'class': 'form-control'}))