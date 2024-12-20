from django.db import models

# Create your models here.


class nav_logo(models.Model):
    logo = models.ImageField(upload_to='static/')


class myname(models.Model):
    name = models.CharField(max_length=100)


class social_media(models.Model):
    linkedin = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)



class profile_photo(models.Model):
    profile = models.ImageField(upload_to='static/')


class about_us(models.Model):
    about_heading = models.CharField(max_length=100)
    about_details = models.TextField()
    my_resume = models.FileField(upload_to='static/')



class education(models.Model):
    degree_name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    degree_compete_year = models.CharField(max_length=200)


class my_skills(models.Model):
    html = models.FileField(upload_to='static/')
    css = models.FileField(upload_to='static/') 
    js = models.FileField(upload_to='static/')
    bootstrap = models.FileField(upload_to='static/')
    python = models.FileField(upload_to='static/')
    django = models.FileField(upload_to='static/')


class projects(models.Model):
    project_image = models.ImageField(upload_to='static/')
    project_name = models.CharField(max_length=200)
    project_detail = models.TextField()
    git_link = models.TextField()


class contact_me(models.Model):
    my_email = models.CharField(max_length=200)
    my_number = models.IntegerField()
