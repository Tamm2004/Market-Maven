from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)

class faq(models.Model):
	question=models.TextField()
	answer=models.TextField()

class latest_news(models.Model):
	headline=models.CharField(max_length=200)
	desc=RichTextField()
	date=models.DateField()
	location=models.TextField()
	writer=models.CharField(max_length=30)
	image=models.ImageField(upload_to="media",blank=True)

class blogs(models.Model):
	title=models.CharField(max_length=200)
	image=models.ImageField(upload_to="media",blank=True)
	desc=RichTextField()
	date=models.DateField()

class tutorials(models.Model):
	title=models.CharField(max_length=200)
	videos=models.FileField()
	
class experts(models.Model):
	name=models.CharField(max_length=50)
	image=models.ImageField(upload_to="media",blank=True)
	address=models.TextField()
	phone_number=models.CharField(max_length=15)
	email_id=models.EmailField()
	description=models.TextField()
	
class myreview(models.Model):
	title=models.CharField(max_length=200)
	message=models.TextField()

class contact_us(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	message=models.TextField()

class helpsupport(models.Model):
	title=models.CharField(max_length=200)
	message=models.TextField()
	

class userregister(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	email=models.EmailField()
	password=models.CharField(max_length=200)
	birthday=models.CharField(max_length=20,blank=True,null=True)
	state=models.CharField(max_length=30,blank=True,null=True)
	country=models.CharField(max_length=30,blank=True,null=True)
	gender=models.CharField(max_length=30,blank=True,null=True)
	pincode=models.CharField(max_length=30,blank=True,null=True)
	address=models.CharField(max_length=1000,blank=True,null=True)
	age=models.CharField(max_length=30,blank=True,null=True)
	contact=models.CharField(max_length=20,blank=True,null=True)
	image=models.ImageField(upload_to="media",blank=True,null=True)

	



	
		


