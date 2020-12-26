from django.contrib import admin

# Register your models here.
from .models import article

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display = ['title','author','createdDate']
    search_fields = ['title']
    list_filter = ['createdDate']
    class Meta:
        model = article