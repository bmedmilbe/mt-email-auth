from django.contrib import admin

from bespoketour.models import BespokeTag, Customer, ProfileTag, ProfileType



class ProfileTagInline(admin.TabularInline):
    model = ProfileTag
    

# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
    list_per_page = 20

@admin.register(ProfileType, BespokeTag)
class ProfileAndTagAdmin(admin.ModelAdmin):
    list_display = ["title", 'image']
    ordering = ["title"]
    list_editable = ["image"]
    
    prepopulated_fields = {"slug": ("title",),"image": ("slug",)}
    search_fields = ["title"]
    inlines = [ProfileTagInline]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user"]
    ordering = ["user"]
    autocomplete_fields = ["profile_type"]










