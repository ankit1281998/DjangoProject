from django.contrib import admin
from .models import UserDetails

# Register your models here.
admin.site.register(UserDetails)

'''@admin.register(UserDetails)
class UserDetailsTable(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password')
    search_fields = ('Username', 'Email')
    list_per_page = 10'''