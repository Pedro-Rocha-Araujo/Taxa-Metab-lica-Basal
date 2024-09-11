from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = [
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
    ]   
    id_usuario = models.AutoField(primary_key=True)
    idade = models.IntegerField(default=0)
    altura = models.FloatField(default=0)
    peso = models.FloatField(default=0) 
    kcal = models.FloatField(default=0)
    sexo = models.CharField(max_length=100, choices=SEXO_CHOICES,default="Masculino")