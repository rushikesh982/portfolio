from django.shortcuts import render
from website import models

# Create your views here.
def home(req):
    data = models.nav_logo.objects.all()
    myname = models.myname.objects.all()
    social_media = models.social_media.objects.all()
    profile_photo = models.profile_photo.objects.all()
    about_us = models.about_us.objects.all()
    education = models.education.objects.all()
    my_skills = models.my_skills.objects.all()
    projects = models.projects.objects.all()
    contact_me = models.contact_me.objects.all()
    obj = {'data':data,'myname':myname,'social_media':social_media,'profile_photo':profile_photo,'about_us':about_us,'education':education,'my_skills':my_skills,'projects':projects,'contact_me':contact_me}
    return render(req,'index.html',obj)