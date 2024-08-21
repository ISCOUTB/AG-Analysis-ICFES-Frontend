from django.contrib import admin
from saber.models import Department, Municipality, Institution, Student, Saber11Results, SaberProResults

models_to_register = [Department, Municipality, Institution, Student, Saber11Results, SaberProResults]

for model in models_to_register:
    admin.site.register(model)

