from django.contrib import admin
from .models import Category,Section,Language,Blog,Blog_Image,Additional_Information,Contact_Us
# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['id','name']
    

@admin.register(Section)
class Section_Admin(admin.ModelAdmin):
    list_display=['id','name']
    

@admin.register(Language)
class Language_Admin(admin.ModelAdmin):
    list_display=['id','language_name']
    

admin.site.register(Blog_Image)
admin.site.register(Additional_Information)


@admin.register(Contact_Us)
class Contact_Admin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','phone']
    
    
class Blog_Images(admin.TabularInline):
    model=Blog_Image

class Additional_Informations(admin.TabularInline):
    model=Additional_Information

class Blog_Admin_add(admin.ModelAdmin):
    inlines=[Blog_Images,Additional_Informations]
    list_display=['id','Category_Selection','Language_Selection','Section_Selection','slug','Date']
    
    
    
admin.site.register(Blog,Blog_Admin_add)
