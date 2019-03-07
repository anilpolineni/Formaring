from django.db import models
from django.forms import ModelForm

# Create your models here.
class farmersignup(models.Model):
	
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	confirmpassword=models.CharField(max_length=100)
	address=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=10,unique=True)
	#gender_op=(('male','Male'),('female','Female'))
	gender=models.CharField(max_length=10)
	isFarmer=models.BooleanField(default=False)
	def __str__(self):
		return str(self.username)
		

class farmerSignupForm(ModelForm):
	class Meta:
		model=farmersignup
		fields=['username','password','confirmpassword','address','phone_no','gender']

class suppliersignup(models.Model):
	
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	confirmpassword=models.CharField(max_length=100)
	address=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=10,unique=True)
	#gender_op=(('male','Male'),('female','Female'))
	gender=models.CharField(max_length=10)
	isSupplier=models.BooleanField(default=False)
	def __str__(self):
		return str(self.username)
		

class supplierSignupForm(ModelForm):
	class Meta:
		model=suppliersignup
		fields=['username','password','confirmpassword','address','phone_no','gender']



class Complaints(models.Model):
	Name=models.CharField(max_length=30)
	complaint=models.CharField(max_length=1000)
	def __str__(self):
		return str(self.Name)

class ComplaintsForm(ModelForm):
	class Meta:
		model=Complaints
		fields=['Name','complaint']

class SellCrop(models.Model):
	SuplierName=models.CharField(max_length=50)
	CropName=models.CharField(max_length=40)
	Quantity=models.CharField(max_length=20)
	Rupees=models.FloatField()
	def __str__(self):
		return str(self.SuplierName)
class SellCropForm(ModelForm):
	class Meta:
		model=SellCrop
		fields=['SuplierName','CropName','Quantity','Rupees']


class FarmingTips(models.Model):
	FarmingName=models.CharField(max_length=50)
	Farming_Description=models.CharField(max_length=1000)
	def __str__(self):
		return str(self.FarmingName)

class FarmingTipsForm(ModelForm):
	model=FarmingTips
	fields=['FarmingName','Farming_Description']
class Upload(models.Model):
	Form_title=models.CharField(max_length=30)
	Form_usage=models.CharField(max_length=30)
	Form_logo=models.FileField()
	def __str__(self):
		return str(self.Form_title)

class UploadForm(ModelForm):
	class Meta:
		model=Upload
		fields=['Form_title','Form_usage','Form_logo']







# Create your models here.
#image=models.FileField()