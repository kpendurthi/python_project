from django.contrib import admin

# Register your models here.
from .models import City, Houses

# Register your models here.
admin.site.register(City)
admin.site.register(Houses)
