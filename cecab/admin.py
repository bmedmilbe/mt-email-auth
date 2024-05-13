from django.contrib import admin
from . import models
# Register your models here.

from datetime import datetime, date


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'picture']
    autocomplete_fields = ['role']

@admin.register(models.Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ['name',  'number_of_associated']
    search_fields = ['name']

@admin.register(models.AssociationImages)
class AssociationImagesAdmin(admin.ModelAdmin):
    list_display = ['associaton', 'image']
    autocomplete_fields = ['associaton']

@admin.register(models.YearGols)
class YearGolsAdmin(admin.ModelAdmin):
    list_display = ['year', 'associations', 'agricultors', 'products']


@admin.register(models.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(models.Pathner)
class PathnerAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(models.Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'subject', 'date']



@admin.register(models.PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ['post', 'picture']
    autocomplete_fields = ['post']
@admin.register(models.PostVideos)
class PostVideosAdmin(admin.ModelAdmin):
    list_display = ['post', 'video']
    autocomplete_fields = ['post']

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    prepopulated_fields = {'slug': ['title']}
    # list_filter = ['doctor'] 
    list_editable = ['active']
    search_fields = ['title']