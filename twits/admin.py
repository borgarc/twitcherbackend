from django.contrib import admin
from twits.models import Twit, Reply

@admin.register(Twit, Reply)
class AuthorAdmin(admin.ModelAdmin):
    pass

