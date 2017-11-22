# -*- coding: utf-8 -*-


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'size':'100','class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'size': '100', 'class': 'form-control'}))
    phon = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'size':'100','class': 'form-control'}))
    message = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'size': '100', 'class': 'form-control'}))
    copy = forms.CharField(required=False)