from django.contrib import admin
from twits.models import Twit

@admin.register(Twit)
class AuthorAdmin(admin.ModelAdmin):
    pass

