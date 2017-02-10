from django.contrib import admin
from .models import UserGoldGroup, UserProfile, LineCgv, Code, Bank

# Register your models here.

admin.site.register(UserGoldGroup)
admin.site.register(UserProfile)
admin.site.register(LineCgv)
admin.site.register(Code)
admin.site.register(Bank)
