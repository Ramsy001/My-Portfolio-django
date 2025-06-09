from django.db import models

# Create your models here.
class ProfileInfo(models.Model):
    image = models.ImageField(null=True,default="images/shelves.jpg")
     
class TechStack(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    ProjectName = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.ProjectName
    
class Experience(models.Model):
    Institution = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)

    def __str__(self):
        return self.Institution

class Ceritifications(models.Model):
    name = models.CharField(max_length=255)
    file  = models.FileField(upload_to='certifications/',null=True)

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    resume = models.FileField(upload_to='resune')