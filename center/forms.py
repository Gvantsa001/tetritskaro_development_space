from django import forms

class JoinForm(forms.Form):
    full_name = forms.CharField(label="სახელი და გვარი", max_length=120)
    email = forms.EmailField(label="ელფოსტა")
    message = forms.CharField(label="როგორ გსურთ ჩართვა?", widget=forms.Textarea, max_length=1500)
