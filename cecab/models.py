from django.db import models
from django.conf import settings

# Create your models here.


class Pathner(models.Model):
    title = models.CharField(max_length=255)  # Presidende/ secretario
    picture = models.FileField(upload_to='cecab/blog/pathner_images')

    def __str__(self) -> str:
        return f'{self.title}'
    

class District(models.Model):
    name = models.CharField(max_length=255)  # Presidende/ secretario

    def __str__(self) -> str:
        return f'{self.name}'

class Role(models.Model):
    title = models.CharField(max_length=255)  # Presidende/ secretario

    def __str__(self) -> str:
        return f'{self.title}'
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    picture = models.FileField(upload_to='cecab/blog/team_images')
    role = models.ForeignKey(Role, on_delete=models.PROTECT)


class Association(models.Model):
    name = models.CharField(max_length=255)  
    registered = models.DateField()
    address = models.CharField(max_length=255)  
    # president_name = models.CharField(max_length=255)
    number_of_associated = models.IntegerField()
    picture = models.FileField(upload_to='cecab/blog/association_images')
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="association")

    def __str__(self) -> str:
        return f'{self.name}'
    
class AssociationImages(models.Model):
    associaton = models.ForeignKey(
        Association, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(upload_to='cecab/blog/association_images')


class YearGols(models.Model):
    year = models.IntegerField()
    associations = models.IntegerField()
    agricultors = models.IntegerField()
    products = models.DecimalField(max_digits=10, decimal_places=2)


class Band(models.Model):
    title = models.CharField(max_length=255) 
    link = models.URLField()
    picture = models.FileField(upload_to='cecab/blog/band_images', null=True, blank=True)
    

class Spot(models.Model):
    title = models.CharField(max_length=255) 
    link = models.URLField()
    created_at = models.DateField()
    picture = models.FileField(upload_to='cecab/blog/band_images', null=True, blank=True)




class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    subject = models.CharField(max_length=255)
    sent = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    picture = models.FileField(upload_to='cecab/blog/post_images')

    text_file = models.FileField(upload_to='cecab/blog/posts')
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.slug}'


class PostImages(models.Model):
    picture = models.FileField(upload_to='cecab/blog/post_images')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_images")
    
class PostVideos(models.Model):
    video = models.URLField(null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_videos", null=True)


class PostDocument(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='cecab/blog/posts')


