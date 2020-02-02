from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'username', 'user__email']
    list_display = ('first_name','phone_number', 'username',)
