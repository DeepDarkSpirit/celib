#coding=utf-8
'''
Created on 2015Äê8ÔÂ11ÈÕ

@author: 201507270151
'''
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
