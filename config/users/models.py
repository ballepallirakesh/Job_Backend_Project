from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Company(models.Model):
    name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    website=models.URLField(blank=True)
    
    def __str__(self):
        return self.name
class Job(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=200)
    salary=models.IntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Application(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    resume=models.TextField()
    applied_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.name} + {self.job.title}"