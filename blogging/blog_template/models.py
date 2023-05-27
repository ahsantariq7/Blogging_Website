from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Category'
        
    
    def __str__(self):
        return self.name
    
 
    
class Language(models.Model):
    language_name=models.CharField(max_length=60)
    class Meta:
        verbose_name_plural = 'Language'
    
    
    def __str__(self):
        return self.language_name

    
class Section(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Section'
    
    
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title=models.CharField(max_length=150)
    Category_Selection=models.ForeignKey(Category,on_delete=models.CASCADE)
    Language_Selection=models.ForeignKey(Language,on_delete=models.CASCADE)
    Section_Selection=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to = "Title_Images",default=False)
    Description=RichTextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    Date=models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = 'Blog'
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog_detail", kwargs={'slug': self.slug})


    class Meta:
        db_table = "app_Blog"
        
        

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Blog)


class Blog_Image(models.Model):
    Blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image=models.ImageField(upload_to = "Blog_Images",default=False)
    class Meta:
        verbose_name_plural = 'Blog_Image'
    
    
    def __str__(self):
        return self.Blog


class Additional_Information(models.Model):
    Blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    written_by=models.CharField(max_length=150)
    References=RichTextField()
    class Meta:
        verbose_name_plural = 'Additional Information'
    
    
    def __str__(self):
        return self.written_by



class Contact_Us(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()
    class Meta:
        verbose_name_plural = 'Contact_Us'
    
    
    def __str__(self):
        return self.first_name+' ' + self.last_name
    
