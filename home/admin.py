from django.contrib import admin

# Register your models here.
from home.models import Member, Feedback

admin.site.register(Member)
admin.site.register(Feedback)
