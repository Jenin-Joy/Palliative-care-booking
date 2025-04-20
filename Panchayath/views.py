from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
# Create your views here.
def homepage(request):
    return render(request,"Panchayath/Panchayathhomepage.html")

def profile(request):
    panchayath=tbl_panchayath.objects.get(id=request.session["pid"])
    return render(request,'Panchayath/Myprofile.html',{'panchayath':panchayath})

def editprofile(request):
     b=tbl_panchayath.objects.get(id=request.session["pid"])
     if request.method=="POST":
        b.panchayath_name=request.POST.get("name")
        b.panchayath_email=request.POST.get("email")
        b.panchayath_contact=request.POST.get("contact")
        b.panchayath_address=request.POST.get("address")
        b.save()
        return redirect("Panchayath:profile")
     else:
         return render(request,"Panchayath/EditProfile.html",{'panchayath':b})
     
def changepassword(request):
     b=tbl_panchayath.objects.get(id=request.session["pid"])
     olda=b.panchayath_password
     oldb=request.POST.get("panchayath_old_password")
     new=request.POST.get("panchayath_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.panchayath_password=request.POST.get("panchayath_new_password")
                b.save()
                return render(request,"Panchayath/Myprofile.html",{"msg":"Password Changed"})
            else:
                return render(request,"Panchayath/Changepassword.html",{"msg":"New Password not matched"})
        else:
            return render(request,"Panchayath/Changepassword.html",{"msg":"Old Password not matched"})
     else:
         return render(request,"Panchayath/Changepassword.html") 

def viewuser(request):
    user=tbl_reg.objects.filter(ward__panchayath=request.session["pid"])
    return render(request,"Panchayath/Viewuser.html",{'user':user})

def addward(request):
    ward = tbl_ward.objects.all()
    panchayathward = tbl_panchayathward.objects.filter(panchayath=request.session["pid"])
    if request.method == "POST":
        wards = request.POST.getlist("txt_ward[]")
        for i in wards:
            count = tbl_panchayathward.objects.filter(panchayath=request.session["pid"],ward=i).count()
            if count > 0:
                return render(request,"Panchayath/Addward.html",{'msg':"ward already added"})
            tbl_panchayathward.objects.create(panchayath=tbl_panchayath.objects.get(id=request.session["pid"]),ward=tbl_ward.objects.get(id=i))
        return redirect("Panchayath:addward")
    return render(request,"Panchayath/Addward.html",{'ward':ward,'panchayathward':panchayathward})

def delward(request,id):
    tbl_panchayathward.objects.get(id=id).delete()
    return redirect("Panchayath:addward")

def viewpaliativecare(request):
    newpaliativecare=tbl_paliativecare.objects.filter(paliativecare_status=0,panchayath=request.session["pid"])
    acceptedpaliativecare=tbl_paliativecare.objects.filter(paliativecare_status=1,panchayath=request.session["pid"])
    rejectedpaliativecare=tbl_paliativecare.objects.filter(paliativecare_status=2,panchayath=request.session["pid"])
    return render(request,"Panchayath/Viewpaliativecare.html",{'newpaliativecare':newpaliativecare,'acceptedpaliativecare':acceptedpaliativecare,'rejectedpaliativecare':rejectedpaliativecare})

def verifypaliativecare(request,id,status):
    data=tbl_paliativecare.objects.get(id=id)
    data.paliativecare_status=status
    data.save()
    return redirect("Panchayath:viewpaliativecare")

def logout(request):
    del request.session["pid"]
    return redirect("Guest:login")