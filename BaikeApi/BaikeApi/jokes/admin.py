from django.contrib import admin
from .models import Joke

# Register your models here.
class JokeAdmin(admin.ModelAdmin):
    list_display = ('content','author')
admin.site.register(Joke,JokeAdmin)