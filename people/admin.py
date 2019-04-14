from django.contrib import admin
from twits.models import Person

@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    pass

