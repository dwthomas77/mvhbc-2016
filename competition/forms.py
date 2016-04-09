from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from competition.models import UserProfile, Address, Submission

# Users
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=75, required=True)
    first_name = forms.CharField(max_length=100, required=True)  
    last_name = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# Judge-centric User Profile
class JudgeUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('judge_preference', 'qualification', 'bjcp_registration', 'judge_comments', 'phone_number', 'club', 'aha_id')

# Profile Info
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('club', 'aha_id')

# Address Info
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields= ('street_1', 'street_2', 'city', 'state', 'zipcode')

# Profile Judge fields
class ProfileJudgeForm(ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
          'judge_comments': forms.Textarea(attrs={'rows':3})
        }
        fields = ('judge_preference', 'qualification', 'bjcp_registration', 'judge_comments')

# Submission Form
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        widgets = {
          'comments': forms.Textarea(attrs={'rows':2})
        }
        fields = ('style', 'name', 'comments')

# AccountUserProfile
class AccountUserProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    club = forms.CharField(label='Club', max_length=200, required=False)
    aha_id = forms.CharField(label='AHA Id', max_length=200, required=False)







