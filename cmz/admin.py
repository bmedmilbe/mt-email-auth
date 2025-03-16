from django.contrib import admin
from . import models
# Register your models here.

from datetime import datetime, date


from django.contrib import admin


class ImagesTourInline(admin.TabularInline):
    model = models.ImagesTour

class InformationInline(admin.TabularInline):
    model = models.Information

class PostImagesInline(admin.TabularInline):
    model = models.PostImages

class PostVideosInline(admin.TabularInline):
    model = models.PostVideos

# class DoctorImageInline(admin.StackedInline):
#     model = models.DoctorImage

# class DoctorIDInline(admin.StackedInline):
#     model = models.DoctorID

@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']

    def get_search_results(self, request, queryset, search_term):
        # Customize the queryset here (e.g., additional filtering)
        # For demonstration purposes, let's filter books published after 2000
        if not request.user.is_superuser:
             queryset = queryset.filter(user__parthner=request.user.parthner)

        # Call the parent method to perform the default search
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # pass
            return qs  # Superusers see all records
        return qs.filter(user__parthner=request.user.parthner)  # Others see only their own records

@admin.register(models.SecreatarySection)
class SecreatarySectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'secretary']
    autocomplete_fields = ['section', 'secretary']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # pass
            return qs  # Superusers see all records
        return qs.filter(secretary__user__parthner=request.user.parthner)  # Others see only their own records



@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
    autocomplete_fields = [ 'role']


@admin.register(models.Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'subject', 'date']


@admin.register(models.Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    search_fields = ['title']
    list_editable = ['active']
    prepopulated_fields = {'slug': ['title']}

    inlines = [
        ImagesTourInline,
    ]

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
    
    inlines = [
        InformationInline,
    ]

# @admin.register(models.Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#     prepopulated_fields = {'slug': ['name']}

#     inlines = [
#         InformationInline,
#     ]
@admin.register(models.Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['service', 'question']
    autocomplete_fields = ["service"]

  


# @admin.register(models.PostImages)
# class PostImagesAdmin(admin.ModelAdmin):
#     list_display = ['post', 'picture']
#     autocomplete_fields = ['post']
# @admin.register(models.PostVideos)
# class PostVideosAdmin(admin.ModelAdmin):
#     list_display = ['post', 'video']
#     autocomplete_fields = ['post']

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'featured']
    prepopulated_fields = {'slug': ['title']}
    # list_filter = ['doctor']
    list_editable = ['active', 'featured']
    search_fields = ['title']

    inlines = [
        PostImagesInline,PostVideosInline
    ]
