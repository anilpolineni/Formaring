from django.shortcuts import render
from django import forms
from . import models
from . models import farmersignup as fSignUp
from . models import suppliersignup as sSignUp
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,login as supplier,logout
# Create your views here.
def home(request):
	return render(request,'home.html')
def contactus(request):
	return render(request,'contactus.html')
def about(request):
	return render(request,'about.html')
# def login(request):	
# 	return render(request,'login.html')
def main(request):
	return render(request,'main.html')
def postadd(request):
	return render(request,'postadd.html')
def crop(request):
	return render(request,'crop.html')
def contact(request):
	return render(request,'contact.html')
def main1(request):
	return render(request,'main1.html')
def complaint(request):
	return render(request,'complaint.html')
def viewcom(request):
	return render(request,'complaintslist.html')
def cropad(request):
	datas1=models.Upload.objects.all()
	return render(request,'cropad.html',{'datas1':datas1})
def upload(request):
	if request.method=='POST':
		datas1=models.UploadForm(request.POST,request.FILES)
		# if request.method==
		try:
			datas1.save()
			return render(request,'main.html',{'msg':'saved'})	
		except:
			return render(request,'dummy.html',{'msg':'not saved'+str(datas1.errors)})
	else:
		datas1=models.UploadForm()
		attrs={'heading':"uploading"}
		return render(request,'uploading.html',{'datas1':datas1,'attrs':attrs})

def sell(request):
	if request.method=='POST':
		datas1=models.SellCropForm(request.POST)
		# if request.method==
		try:
			datas1.save()
			return render(request,'main1.html',{'msg':'saved'})	
		except:
			return render(request,'dummy.html',{'msg':'not saved'+str(datas1.errors)})
	else:
		datas1=models.SellCropForm()
		attrs={'heading':"SellCrop"}
		return render(request,'ss.html',{'datas1':datas1,'attrs':attrs})			


def suppliersignup(request):
	if request.method=='POST':
		datas=models.supplierSignupForm(request.POST)
		# if request.method=='POST':
		username=request.POST.get('username').strip()
		phone_no=request.POST.get('phone_no')
		password=request.POST.get('password').strip()
		confirmpassword=request.POST.get('confirmpassword')
		address=request.POST.get('address')
		gender=request.POST.get('gender')
		if (username!=""):
			email=username+"@mysupplier.com"

			if(password==confirmpassword):
				print("saving start")
				try:
					user=User.objects.create_user(username=username,email=email,password=password)
				except Exception as e:
					print(e)
					return HttpResponse("username "+str(username)+" already available try with another name")
				try:
					#datas.save()
					ssign=sSignUp(username=username,password=password,confirmpassword=confirmpassword,phone_no=phone_no,address=address,gender=gender,isSupplier=True)
					
					ssign.save()
					print("saving end")

					return render(request,'home.html',{'msg':'saved'})	
				except Exception as e:
					print(e)
					return render(request,'dummy.html',{'msg':'sorry not saved'+str(datas.errors)})
			else:
				attrs={'btnValue':"Register",'heading':'NewUserSign-in','msg':"password doesn't match, please try again"}
				return render(request,'suppliersignup.html',{'datas':datas,'attrs':attrs})
		else:
			msg="Username cannot be null"
			return render(request,'msg.html',{'msg':msg})
	else:
		datas=models.supplierSignupForm()
		print(str(datas.errors))
		attrs={'btnValue':"Register",'heading':'NewUserSign-in'}
		return render(request,'suppliersignup.html',{'datas':datas,'attrs':attrs})


def farmersignup(request):
	if request.method=='POST':
		#datas1=models.farmerSignupForm(request.POST)
		# if request.method=='POST':
		username=request.POST.get('username').strip()
		password=request.POST.get('password')
		confirmpassword=request.POST.get('confirmpassword')
		address=request.POST.get('address')
		gender=request.POST.get('gender')
		phone_no=request.POST.get('phone_no')
		if (username!=""):
			email=username+"@myfarm.com"
			if(password==confirmpassword):
				try:
					user=User.objects.create_user(username,email,password)
				except Exception as e:
					print(e)
					return HttpResponse("username "+str(username)+" already available try with another name")
				try:
					#datas1.save()
					fsign=fSignUp(username=username,password=password,confirmpassword=confirmpassword,phone_no=phone_no,address=address,gender=gender,isFarmer=True)
					fsign.save()
					return render(request,'home.html',{'msg':'saved'})	
				except:
					return render(request,'dummy.html',{'msg':'not saved'+str(datas.errors)})
			else:
				attrs={'btnValue':"Register",'heading':'NewUserSign-in','msg':"password doesn't match, please try again"}
				return render(request,'farmersignup.html',{'datas1':datas1,'attrs':attrs})
		else:
			msg="Username cannot be null"
		return render(request,'msg.html',{'msg':msg})
	else:
		datas1=models.farmerSignupForm()
		print(str(datas1.errors))
		attrs={'btnValue':"Register",'heading':'NewUserSign-in'}
		return render(request,'farmersignup.html',{'datas1':datas1,'attrs':attrs})		
def farmersignin(request):
	if request.user.is_authenticated:
		msg="models "+request.user.username+" is already in logged in state"
		return render(request,'msg.html',{'msg':msg})
	if request.method=='POST':
		uname=request.POST.get('username').strip()
		pword=request.POST.get('password').strip()
		user=authenticate(username=uname,password=pword)
		userobject=fSignUp.objects.filter(username=uname,password=pword)
		#allusers=User.objects.filter(username=uname,password=pword)
		allusers=User.objects.filter(username=uname)
		print(allusers)
		print(uname)
		print(pword)
		if len(allusers)==1:
			if len(userobject)==1:
				if userobject[0].isFarmer:
					if user is None:
						msg="login failed"+uname+","+pword	
						return render(request,'msg.html',{'msg':msg})
		
					else:
						main="login success"
						login(request,user)			
						return render(request,'main1.html',{'main':main})
				else:
					return HttpResponse("you are not a farmer")
				#attrs={'btnValue':"Login",'heading':'Farmer Sign-in'}
				#return render(request,'farmersignin.html',{'attrs':attrs})
			else:
				return HttpResponse("you are not a farmer")
		else:
			return HttpResponse("user not found")
	else:
		attrs={'btnValue':"Login",'heading':'Farmer Sign-in'}
		return render(request,'farmersignin.html',{'attrs':attrs})
def suppliersignin(request):
	if request.user.is_authenticated:
		msg="User "+request.user.username+" is already in logged in state"
		return render(request,'msg.html',{'msg':msg})
	if request.method=='POST':
		uname=request.POST.get('username')
		pword=request.POST.get('password')
		user=authenticate(username=uname,password=pword)
		allusers=User.objects.filter(username=uname)
		print(allusers)
		print(uname)
		print(pword)
		if len(allusers)==1:
			userobject=sSignUp.objects.filter(username=uname)
			if len(userobject)==1:
				if userobject[0].isSupplier:
					if user is None:
						msg="login failed"+uname+","+pword	
						return render(request,'msg.html',{'msg':msg})
					else:
						main="login success"
						supplier(request,user)
						return render(request,'main.html',{'main':main})
				else:
					return HttpResponse("you are not a supplier")
			else:
				return HttpResponse("you are not a supplier")
		else:
			return HttpResponse("user not found")
	else:
		attrs={'btnValue':"Login",'heading':'Supplier Sign-in'}
		return render(request,'suppliersignin.html',{'attrs':attrs})


def complaintpage(request):
	if request.method=='POST':
		datas1=models.ComplaintsForm(request.POST)
		# if request.method==
		try:
			datas1.save()
			return render(request,'main1.html',{'msg':'saved'})	
		except:
			return render(request,'dummy.html',{'msg':'not saved'+str(datas1.errors)})
	else:
		datas1=models.ComplaintsForm()
		attrs={'heading':"ComPlaint"}
		return render(request,'s.html',{'datas1':datas1,'attrs':attrs})			
def FarmingTipsList(request):
	datas=models.FarmingTips.objects.all()
	return render(request,'FarmingTipsList.html',{'datas':datas})

def ComplaintsList(request):
	datas=models.Complaints.objects.all()
	return render(request,'complaintslist.html',{'datas':datas})
def SellCropList(request):
	datas=models.SellCrop.objects.all()
	return render(request,'sellcroplist.html',{'datas':datas})	
def signout(request):
	if request.user.is_authenticated:
		msg="User "+request.user.username+" is succesfully logged out"
		logout(request)	
	else:
		msg="No login present"
	return render(request,'home.html',{'home':home})

# Create your views here.
