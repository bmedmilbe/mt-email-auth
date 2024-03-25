from django.db import models
from django.conf import settings
import pathlib

# from ormed.utils.storage_backends import PublicMediaStorage
# Create your models here.

def  _profile_avatar_upload_path(instance, filename):
    """Provides a clean upload path for user avatar images
    """
    file_extension = pathlib.Path(filename).suffix
    return f'avatars/profiles/{instance.user.username}{file_extension}'

def  _image_doctor_upload_path(instance, filename):
    
    """Provides a clean upload path for doctor images
    """
    file_extension = pathlib.Path(filename).suffix
    return path('doctors/images/',filename,file_extension)
def  _id_doctor_upload_path(instance, filename):
    """Provides a clean upload path for doctor ids
    """
    file_extension = pathlib.Path(filename).suffix
    return path('doctors/ids/',filename,file_extension)
def  _image_post_upload_path(instance, filename):
    """Provides a clean upload path for post images
    """
    file_extension = pathlib.Path(filename).suffix
    return path('posts/images', filename, file_extension)
def  _text_post_upload_path(instance, filename):
    """Provides a clean upload path for post texts
    """
    file_extension = pathlib.Path(filename).suffix
    return path('posts/texts/',filename,file_extension)
def  _image_gallery_upload_path(instance, filename):
    """Provides a clean upload path for gallery images
    """
    file_extension = pathlib.Path(filename).suffix
    return path('gallerys/images/', filename, file_extension)
def  _document_law_upload_path(instance, filename):


    """Provides a clean upload path for law documents
    """
    file_extension = pathlib.Path(filename).suffix
    return path('laws/documents/', filename, file_extension)

def path(path, filename, file_extension):
    # return  f'blog/{path}'
    # return  f'{path}/{filename}'
    # if settings.DEBUG:
    #    return  f'{path}'
    return f'blog/{path}/{filename}'

class Section(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.title}'


class UserSection(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="user_sections")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Level(models.Model):
    title = models.CharField(max_length=255)  # infermeiro/doutor/especialista

    def __str__(self) -> str:
        return f'{self.title}'


class Area(models.Model):
    title = models.CharField(max_length=255)  # genecologista/parteira...

    def __str__(self) -> str:
        return f'{self.title}'


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'


class IdType(models.Model):
    name = models.CharField(max_length=255)  # passport/bi/

    def __str__(self) -> str:
        return f'{self.name}'


# class DoctorImage(models.Model):
#     picture = models.FileField(upload_to=_image_doctor_upload_path)


# class DoctorDocumentImage(models.Model):
#     document = models.FileField(upload_to=_id_doctor_upload_path)


class Doctor(models.Model):
    # name = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    level = models.ForeignKey(Level, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    birth_date = models.DateField()
    bio = models.TextField()
    # picture = models.URLField(null=True)
    # picture = models.OneToOneField(DoctorImage, on_delete=models.PROTECT)
    # document = models.OneToOneField(
    #     DoctorDocumentImage, on_delete=models.PROTECT)
    # document = models.URLField(null=True)

    id_type = models.ForeignKey(IdType, on_delete=models.PROTECT, null=True)
    id_number = models.CharField(max_length=255, null=True)
    id_valid = models.DateField(null=True)

    verified = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    

   
    picture = models.FileField(upload_to='ormed/doctors/images/', null=True, blank=True)
    document = models.FileField(upload_to='ormed/doctors/ids/', null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.user.last_name}'

    # People register and create account, can update details after


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class ImagesGallery(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name="images")

    # image = models.URLField()
    image = models.FileField(upload_to='ormed/gallerys/images/')


class Law(models.Model):

    file = models.FileField(upload_to='ormed/laws/documents/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)

    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.slug}'


class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.ForeignKey(Section, on_delete=models.PROTECT)
    text = models.TextField()
    sent = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class PostFile(models.Model):
    file = models.FileField(upload_to='ormed/posts/images/')


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    picture = models.FileField(upload_to='ormed/posts/images/')
    # doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)

    text_file = models.FileField(upload_to='ormed/posts/documents/')
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    # post_images = models.CharField(max_length=255, null=True)
    # post_videos = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f'{self.title}'


class PostImages(models.Model):
    picture = models.FileField(upload_to='ormed/posts/images/')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_images")
class PostVideos(models.Model):
    video = models.URLField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_videos")





class PostDocument(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='ormed/post/documents/')


class Role(models.Model):
    title = models.CharField(max_length=255)  # Presidende/ secretario

    def __str__(self) -> str:
        return f'{self.title}'


class Team(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    class Meta():
        unique_together = ['doctor']

    def __str__(self) -> str:
        return f'{self.doctor.user.first_name} - {self.role.title}'
