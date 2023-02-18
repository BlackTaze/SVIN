from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Основная часть")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

class Rules(models.Model):
    content = models.TextField(null=True, verbose_name="Правила")
    
    
class Review(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")
    content = models.TextField( verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
            
            
             
    

    
        

    
    

