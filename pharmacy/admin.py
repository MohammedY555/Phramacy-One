from django.contrib import admin
from pharmacy.models import UserCure, Cure

admin.site.register(Cure)
admin.site.register(UserCure)
