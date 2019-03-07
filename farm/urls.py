from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='farm'
urlpatterns=[
path('FarmingTipsList/',views.FarmingTipsList,name='FarmingTipsList'),
path('ComplaintsList/',views.ComplaintsList,name='ComplaintsList'),
path('SellCropList/',views.SellCropList,name='SellCropList'),
path('',views.home,name='home'),
path('contactus/',views.contactus,name='contactus'),
path('farmersignin/',views.farmersignin,name='farmersignin'),
path('suppliersignin/',views.suppliersignin,name='suppliersignin'),

path('farmersignup/',views.farmersignup,name='farmersignup'),
path('suppliersignup/',views.suppliersignup,name='suppliersignup'),
# path('signup/',views.signup,name='signup'),
path('about/',views.about,name='about'),
path('main/',views.main,name='main'),
path('postadd/',views.postadd,name='postadd'),
path('crop/',views.crop,name='crop'),
path('main1/',views.main1,name='main1'),
path('complaint/',views.complaintpage,name='complaint'),
path('viewcom/',views.viewcom,name='viewcom'),
path('cropad/',views.cropad,name='cropad'),
path('sell/',views.sell,name='sell'),
path('signout/',views.signout,name='signout'),
path('upload/',views.upload,name='upload'),
]












