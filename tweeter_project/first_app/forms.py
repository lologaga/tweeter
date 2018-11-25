from django import forms
from django.core import validators
from first_app.models import User, Tweet


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'


'''class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_date = super().clean()
        email = all_clean_date['email']
        verify_email = all_clean_date['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Make sure emails are the same')'''


