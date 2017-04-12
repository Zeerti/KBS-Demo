from django import forms
from django.utils.translation import ugettext_lazy as _ #Translates, used in ValidationError checking
import datetime #for checking renewal date range.
from markdownx.fields import MarkdownxFormField
from markdownx.widgets import MarkdownxWidget

class MyForm(forms.Form):
    body = MarkdownxFormField(widget=MarkdownxWidget(attrs={'class':'custom-class-body'}))
    #markdownx_form_field2 = MarkdownxFormField(widget=MarkdownxWidget(attrs={'class':'custom-class-markdownx_form_field2'}))