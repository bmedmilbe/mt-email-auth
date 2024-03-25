from django.db import models
from django.conf import settings
import pathlib

def path(path, filename, file_extension):
    # return  f'blog/{path}'
    # return  f'{path}/{filename}'
    # if settings.DEBUG:
    #    return  f'{path}'
    return f'blog/{path}/{filename}'

class Secretary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}' 

class Section(models.Model):
    title = models.CharField(max_length=255)
    # gando, financa, camara, obra, cimiterio
    def __str__(self) -> str:
        return f'{self.title}'    

class SecreatarySection(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="secreatary_sections")
    secretary = models.ForeignKey(Secretary,
                             on_delete=models.CASCADE)
    
    


class Tour(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    description = models.TextField()
    location = models.URLField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class ImagesTour(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name="images")

    # image = models.URLField()
    image = models.FileField(upload_to='camaramz/tour/images/')


class PostFile(models.Model):
    file = models.FileField(upload_to='camaramz/posts/file/')


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    picture = models.FileField(upload_to='camaramz/posts/images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    text_file = models.FileField(upload_to='camaramz/posts/documents/', null=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    # post_images = models.CharField(max_length=255, null=True)
    # post_videos = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
class PostDocument(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='camaramz/post/documents/')


class PostImages(models.Model):
    picture = models.FileField(upload_to='camaramz/posts/images/')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_images")
class PostVideos(models.Model):
    video = models.URLField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_videos")



class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    sent = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Service(models.Model):
    name = models.CharField(max_length=255)  
    slug = models.SlugField(max_length=255)  
    picture = models.FileField(upload_to='camaramz/services/images/', null=True)
    description = models.TextField(default="Através desse seviço, estarás habilitado para ...")
    def __str__(self) -> str:
        return f'{self.name}'

class Information(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="informations")
    information = models.TextField() 
    question = models.CharField(max_length=255) 
    def __str__(self) -> str:
        return f'{self.question}'
    
class Role(models.Model):
    title = models.CharField(max_length=255)  

    def __str__(self) -> str:
        return f'{self.title}'

class Team(models.Model):
    name = models.CharField(max_length=255)  
    image = models.FileField(upload_to='camaramz/team/images/', null=True)  
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    class Meta():
        unique_together = ['name', 'role']

    def __str__(self) -> str:
        return f'{self.name} - {self.role.title}'
