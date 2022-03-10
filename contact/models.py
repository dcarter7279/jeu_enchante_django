from email import message
from django.db import models
from validators import email

# Create your models here.
class Contact(models.Model):
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField(max_length=5000)

	def __str__(self):
		return self.email