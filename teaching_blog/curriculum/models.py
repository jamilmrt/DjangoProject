from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

import os



# Create your models here.

class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null= True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
def save_subject_image(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)


class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100,)
    slug = models.SlugField(null= True, blank=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
    image = models.ImageField(upload_to='subjects')
    description = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)

def save_lesson_files(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
    return os.path.join(upload_to, filename)         
        
class Lesson(models.Model):
    lession_id = models.CharField(max_length=100, unique=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250)
    positon = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null= True, blank=True)
    video = models.FileField(upload_to='videos', verbose_name='Video',blank='True', null='True')
    ppt = models.FileField(upload_to='ppt', verbose_name='Presentation',blank='True', null='True')
    Notes = models.FileField(upload_to='notes', verbose_name='Notes',blank='True', null='True')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['positon']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        


