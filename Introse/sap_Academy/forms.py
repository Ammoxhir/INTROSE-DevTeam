from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sap_Academy.models import Students


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    work_position = forms.CharField()
    employee_num = forms.IntegerField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'work_position',
            'employee_num',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.work_position = self.cleaned_data['work_position']
        user.employee_num = self.cleaned_data['employee_num']
        if commit:
            user.save()

        return user
