from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_Adminreg(models.Model):
    adminreg_name=models.CharField(max_length=50)
    adminreg_email=models.CharField(max_length=50)
    adminreg_password=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_ward(models.Model):
    ward_number=models.IntegerField()




