from django.contrib.auth import authenticate
from django import forms
from myapp.models import *

class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','number','email','password']

class contactform(forms.ModelForm):
    class Meta:
        model = message
        fields = ['user_name','email','message']
       

class trainerform(forms.ModelForm):
    class Meta:
        model = trianer
        fields = ['name','number','email']    
 
class productform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','price','quantity','description']
       

class membershipform(forms.ModelForm):
    class Meta:
        model = membership
        fields = ['name','price','total_day']

class yogaclassform(forms.ModelForm):
    class Meta:
        model = yoga_class
        fields = ['yoga_trainer_name','price','total_day','time']
       
class adminform(forms.ModelForm):
    class Meta:
        model = admin
        fields = ['username','number','email','password'] 

class userpurchasemembership(forms.ModelForm):
    class Meta:
        model = membership_holders
        fields = ['membership_type','membership_price','membership_total_day','user_name','user_email']


class yogaclassbookmember(forms.ModelForm):
    class Meta:
        model = yoga_class_member
        fields = ['trainer_name','class_price','total_day','class_time','user_name','user_email']


class userorderform(forms.ModelForm):
    class Meta:
        model = order
        fields = ['product_id','product_name','product_price','product_quantity','user_name','user_email','user_address','user_city','user_state','user_country']


class cartform(forms.ModelForm):
    class Meta:
        model = cart
        fields = ['product_id','product_name','product_price','product_quantity']


class shipingform(forms.ModelForm):
    class Meta:
        model = shiping
        fields = ['user_name','user_email','user_number','user_address','user_city','user_state','user_country']


class hiretrainerform(forms.ModelForm):
    class Meta:
        model = hiretrainer
        fields = ['trainer_id','trainer_name','trainer_number','trainer_email','total_day','user_name','user_email']