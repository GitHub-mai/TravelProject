'''
from django.contrib import admin
from .models import Users, Destinations


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id')


admin.site.register(Users)
admin.site.register(Destinations, UsersAdmin)
'''