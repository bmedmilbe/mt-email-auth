from django.contrib import admin
from . import models
# Register your models here.

from datetime import datetime, date


from django.contrib import admin

admin.site.site_header = "ORMED-STP Admin"
admin.site.index_title = "Painel de Gestão"


class ImagesGalleryInline(admin.TabularInline):
    model = models.ImagesGallery

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


@admin.register(models.UserSection)
class UserSectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'user']
    autocomplete_fields = ['section', 'user']


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.IdType)
class IdTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'level', 'area',
                    'birth_date', 'bio', 'id_type', 'id_number', 'id_status']
    search_fields = ['name']
    autocomplete_fields = ['country', 'area', 'id_type', 'user']
    ordering = ['level', 'area', 'birth_date', 'country']
    list_filter = ['create_at', 'verified',
                   'country', 'level', 'area']
    
    # def get_search_results(self, request, queryset, search_term):
    #     # Customize the queryset here (e.g., additional filtering)
    #     # For demonstration purposes, let's filter books published after 2000
    #     if not request.user.is_superuser:
    #          queryset = queryset.filter(user__parthner=request.user.parthner)

    #     # Call the parent method to perform the default search
    #     queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #     return queryset, use_distinct
    
    # inlines = [
    #     DoctorImageInline, DoctorImageInline
    # ]

    @admin.display(ordering='name')
    def name(self, doctor: models.Doctor):
        return f'{doctor.user.first_name} {doctor.user.last_name}'
        pass

    def id_status(self, doctor: models.Doctor):
        return "Válido" if doctor.id_valid >= date.today() else "Expirado"


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'role']
    autocomplete_fields = ['doctor', 'role']


@admin.register(models.Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'subject', 'date']


@admin.register(models.Law)
class LawsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ['title']}

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    search_fields = ['title']
    list_editable = ['active']
    prepopulated_fields = {'slug': ['title']}

    inlines = [
        ImagesGalleryInline,
    ]


@admin.register(models.ImagesGallery)
class ImagesGalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'image']
    autocomplete_fields = ['gallery']


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
    list_display = ['title', 'active']
    prepopulated_fields = {'slug': ['title']}
    # list_filter = ['doctor']
    list_editable = ['active']
    search_fields = ['title']

    inlines = [
        PostImagesInline,PostVideosInline
    ]
