from django import forms

class SendRequestForm(forms.Form):
    send_req = forms.CharField(max_length=50)
    