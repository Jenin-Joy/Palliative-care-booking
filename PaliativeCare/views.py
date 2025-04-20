from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.


def homepage(request):
    return render(request,"PaliativeCare/Homepage.html")
def profile(request):
    user=tbl_paliativecare.objects.get(id=request.session["plid"])
    return render(request,'PaliativeCare/Myprofile.html',{'paliativecare':user})

def editprofile(request):
     b=tbl_paliativecare.objects.get(id=request.session["plid"])
     if request.method=="POST":
        b.paliativecare_name=request.POST.get("name")
        b.paliativecare_email=request.POST.get("email")
        b.paliativecare_contact=request.POST.get("contact")
        b.paliativecare_address=request.POST.get("address")
        b.save()
        return redirect("PaliativeCare:profile")
     else:
         return render(request,"PaliativeCare/EditProfile.html",{'paliativecare':b})
     
def changepassword(request):
     b=tbl_paliativecare.objects.get(id=request.session["plid"])
     olda=b.paliativecare_password
     oldb=request.POST.get("user_old_password")
     new=request.POST.get("user_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.paliativecare_password=request.POST.get("user_new_password")
                b.save()
                return render(request,"PaliativeCare/Myprofile.html",{"msg":"Password Changed"})
            else:
                return render(request,"PaliativeCare/Changepassword.html",{"msg":"New Password not matched"})
        else:
            return render(request,"PaliativeCare/Changepassword.html",{"msg":"Old Password not matched"})
     else:
         return render(request,"PaliativeCare/Changepassword.html")  

def viewbooking(request):
    book = tbl_request.objects.filter(paliativecare_id=request.session["plid"]).order_by('-id')
    return render(request, "PaliativeCare/viewbooking.html",{"book":book})

def rejectrequest(request, id):
    req = tbl_request.objects.get(id=id)
    req.request_status = 2
    req.save()
    return render(request,"PaliativeCare/viewbooking.html",{"msg":"Request Rejected"})

def addamount(request, id):
    req = tbl_request.objects.get(id=id)
    if request.method == "POST":
        req.request_status = 1
        req.request_amount = request.POST.get("txt_amount")
        req.request_team = request.POST.get("txt_team")        
        req.save()
        return render(request,"PaliativeCare/viewbooking.html",{"msg":"Request Accepted"})
    return render(request,"PaliativeCare/AddAmount.html")

def logout(request):
    del request.session["plid"]
    return redirect("Guest:login")