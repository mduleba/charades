from django import forms

class modeselect(forms.Form):
    cc_myself = forms.BooleanField(required=False)