from django import forms

# class NameForm(forms.Form):
#     your_name=forms.CharField(label="Your Name", max_length=100)

class NameForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)