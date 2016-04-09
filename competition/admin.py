from django.contrib import admin
from competition.models import UserProfile, Style, Submission, JudgingTable, Address

# Register your models here.
admin.site.register(JudgingTable)
admin.site.register(Style)
admin.site.register(Submission)
admin.site.register(UserProfile)
admin.site.register(Address)