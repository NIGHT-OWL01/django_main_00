from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=20)

	def __str__(self):
		return self.name
class song(models.Model):
	title=models.CharField(max_length=20)
	user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title
