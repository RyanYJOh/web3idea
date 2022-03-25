from django.contrib import admin
from .models import Verbs

# Register your models here.
class ApiAdmin(admin.ModelAdmin):
    readonly_fields = ('id'),

admin.site.register(Verbs)