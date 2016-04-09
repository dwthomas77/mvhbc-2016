from django.db import models
from django.contrib.auth.models import User
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USStateField, PhoneNumberField

# Create your models here.

# Address
class Address(models.Model):
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField(choices = US_STATES)
    zipcode = models.CharField(max_length=5)
    def __unicode__(self):
        name = self.street_1 + ' ' + self.city + ', ' + self.state
        return name

# Styles
class Style(models.Model):
    style_id = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    table = models.ForeignKey('JudgingTable', blank=True, null=True)
    def __unicode__(self):
        name = self.style_id + ' ' + self.name
        return name

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.OneToOneField(Address, blank=True, null=True)
    club = models.CharField(max_length=200, blank=True)
    aha_id = models.CharField(max_length=200, blank=True, verbose_name='AHA ID')
    insert_date =  models.DateField('Registered On', auto_now_add=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    # Judge/Steward related entries
    #
    PREF_CHOICES = (
        ('None', '.....'),
        ('Steward', 'Steward'),
        ('Judge', 'Judge')
    )
    QUALIFICATION_CHOICES = (
        ('None', '.....'),
        ('Apprentice', 'Apprentice'),
        ('Certified', 'Certified'),
        ('Recognized', 'Recognized'),
        ('National', 'National'),
        ('Master', 'Master'),
        ('Grand Master', 'Grand Master'),
        ('Professional Brewer', 'Professional Brewer'),
    )
    judge_preference = models.CharField(max_length=200, blank=True, choices=PREF_CHOICES, default='None')
    qualification = models.CharField(max_length=200, blank=True, choices=QUALIFICATION_CHOICES, default='None')
    bjcp_registration = models.CharField(max_length=100, blank=True, verbose_name='BJCP Registration ID')
    cat_pref_yes = models.ManyToManyField(Style, verbose_name='Categories Preferred To Judge', blank=True, null=True, related_name='yes+')
    cat_pref_no = models.ManyToManyField(Style, verbose_name='Categories Preferred Not To Judge', blank=True, null=True, related_name='no+')
    judge_comments = models.TextField(blank=True, null=True, verbose_name='Comments/Special Reqeusts')
    # display name
    def __unicode__(self):
        name = self.user.last_name + ", " + self.user.first_name
        return name

# Submission
class Submission(models.Model):
    competition_id = models.CharField(max_length=20, blank=True)
    paid = models.BooleanField(default=False)
    name = models.CharField(max_length=200, blank=True)
    comments = models.TextField(blank=True)
    check_in = models.DateField(blank=True, null=True)
    received = models.DateField(blank=True, null=True)
    score = models.CharField(max_length=20, blank=True)
    place = models.CharField(max_length=200, blank=True)
    brewer = models.ForeignKey(UserProfile, blank=True)
    style = models.ForeignKey(Style, blank=True)
    def __unicode__(self):
        name = self.competition_id + ' - ' + self.brewer.user.first_name + ' ' + self.brewer.user.last_name
        return name

# Table
class JudgingTable(models.Model):
    name = models.CharField(max_length=200, blank=True)
    MY_SESSIONS = (
        'AM', 'AM Session',
        'PM', 'PM Session',
    )
    session = models.CharField(max_length=200, blank=True, default='AM')
    locked = models.BooleanField(default=False)
    judges = models.ManyToManyField(UserProfile, related_name='judges')
    stewards = models.ManyToManyField(UserProfile, related_name='stewards')
    def __unicode__(self):
        name = self.name
        return name




