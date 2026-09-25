from django.contrib import admin
from .models import Flan,ContactForm

admin.site.register(ContactForm)

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'precio', 'is_private')
    list_filter = ('tag', 'is_private')
    search_fields = ('name', 'description')