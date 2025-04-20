from django.db import models
from Admin.models import *

class tbl_panchayath(models.Model):
    panchayath_name=models.CharField(max_length=50)
    panchayath_email=models.CharField(max_length=50)
    panchayath_contact=models.CharField(max_length=50)
    panchayath_address=models.CharField(max_length=50)
    panchayath_password=models.CharField(max_length=50)
    panchayath_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    panchayath_photo=models.FileField(upload_to='Assets/panchayath/photo/')
    panchayath_proof=models.FileField(upload_to='Assets/panchayath/proof/')

class tbl_paliativecare(models.Model):
    paliativecare_name=models.CharField(max_length=50)
    paliativecare_email=models.CharField(max_length=50)  
    paliativecare_contact=models.CharField(max_length=50)  
    paliativecare_address=models.CharField(max_length=50)   
    paliativecare_photo=models.FileField(upload_to="Assets/paliativecare/photo/")
    paliativecare_proof=models.FileField(upload_to="Assets/paliativecare/photo/")  
    paliativecare_password=models.CharField(max_length=50) 
    paliativecare_status=models.IntegerField(default=0)
    panchayath=models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)

class tbl_panchayathward(models.Model):
    panchayath=models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)
    ward=models.ForeignKey(tbl_ward,on_delete=models.CASCADE)
    
class tbl_reg(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='Assets/user/photo/',default='Assets/user/photo/img.jpg', null=True)
    user_password=models.CharField(max_length=50)
    ward=models.ForeignKey(tbl_panchayathward,on_delete=models.CASCADE,null=True)