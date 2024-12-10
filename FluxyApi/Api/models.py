from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError

# Create your models here.

# Create your models here.
class Stagiaires(models.Model):
   
    nom=models.CharField(max_length=45,blank=False,null=False)
    prenom=models.CharField(max_length=45,blank=False,null=False)
    email=models.EmailField()
    telephone=models.CharField(max_length=12,null=False,blank=False)
    def __str__(self):
        return self.nom
    
    
class Post(models.Model):
   
    post_name=models.CharField(max_length=120,null=False,blank=False)
    def __str__(self):   
       return self.post_name




class Employee(models.Model):
   
    name=models.CharField(max_length=45,blank=False,null=False)
    surname=models.CharField(max_length=45,blank=False,null=False)
    email=models.EmailField()
    telephone=models.CharField(max_length=12,null=False,blank=False)
   # title=models.CharField(max_length=255,null=False,blank=False)
    gender=models.CharField(max_length=50, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    salary=models.CharField(max_length=255,null=False,blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    adress=models.CharField(max_length=255,null=False,blank=False)
    typecontrat=models.CharField(max_length=255,null=False,blank=False)

    contrat=models.FileField(upload_to='pdf_contrats/')
    hiring_date=models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='pdf_contrats/', null=True, blank=True) 
   
    def __str__(self):
        return self.name




    
    



