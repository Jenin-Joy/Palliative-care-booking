from django.db import models
from Guest.models import *


# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=200)
    complaint_reply=models.CharField(max_length=200)
    user = models.ForeignKey(tbl_reg, on_delete=models.CASCADE,null=True)
    complaint_status=models.IntegerField(default=0)

class tbl_patient(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_age=models.CharField(max_length=50)
    patient_height=models.CharField(max_length=50)
    patient_weight=models.CharField(max_length=50)
    patient_gender=models.CharField(max_length=50)
    patient_gender = models.CharField(max_length=10, choices=[('Male', 'Male'),('Female', 'Female'),])
    patient_description = models.TextField()
    user = models.ForeignKey(tbl_reg, on_delete=models.CASCADE, null=True)

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_fromdate=models.DateField()
    request_todate=models.DateField()
    request_status=models.IntegerField(default=0)
    request_amount=models.CharField(max_length=50)
    request_description=models.CharField(max_length=150)
    patient_id=models.ForeignKey(tbl_patient, on_delete=models.CASCADE,null=True)
    paliativecare_id=models.ForeignKey(tbl_paliativecare, on_delete=models.CASCADE,null=True)
    request_team=models.CharField(max_length=150)

class tbl_rating(models.Model):
    user_id=models.ForeignKey(tbl_reg, on_delete=models.CASCADE,null=True)
    paliativecare_id=models.ForeignKey(tbl_paliativecare, on_delete=models.CASCADE,null=True)
    rating_data=models.IntegerField()
    user_review=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)