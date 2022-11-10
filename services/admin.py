from django.contrib import admin

# Register your models here.
from services.models import ServicesCategory, Transcrib

admin.site.register(ServicesCategory)
admin.site.register(Transcrib)