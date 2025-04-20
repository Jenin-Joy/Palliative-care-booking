from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*


# Create your views here.
def index(request):
    return render(request,'Guest/index.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(email,password)
        usercount=tbl_reg.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_Adminreg.objects.filter(adminreg_email=email,adminreg_password=password).count()
        Panchayathcount=tbl_panchayath.objects.filter(panchayath_email=email,panchayath_password=password).count()
        paliativecarecount=tbl_paliativecare.objects.filter(paliativecare_email=email,paliativecare_password=password).count()
        
        
        if usercount > 0:
            user=tbl_reg.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect("User:homepage")
        
        elif admincount > 0:
            admin=tbl_Adminreg.objects.get(adminreg_email=email,adminreg_password=password)
            request.session["aid"]=admin.id
            return redirect("Admin:homepage")
        
        elif Panchayathcount > 0:
            Panchayath=tbl_panchayath.objects.get(panchayath_email=email,panchayath_password=password)
            if Panchayath.panchayath_status==0:
                return render(request,'Guest/login.html',{"msg":"wait for admin approval"})
            elif Panchayath.panchayath_status==2:
                return render(request,'Guest/login.html',{"msg":"Rejected"})
            else:
                request.session["pid"]=Panchayath.id
                return redirect("Panchayath:homepage")    
           
        elif paliativecarecount > 0:
            paliativecare=tbl_paliativecare.objects.get(paliativecare_email=email,paliativecare_password=password)
            if paliativecare.paliativecare_status==0:
                return render(request,'Guest/login.html',{"msg":"wait for admin approval"})
            elif paliativecare.paliativecare_status==2:
                return render(request,'Guest/login.html',{"msg":"Rejected"})
            else:
                request.session["plid"]=paliativecare.id
                return redirect("PaliativeCare:homepage")
        
        else:
            return render(request,'Guest/login.html',{"msg":"invalid data"})
    else:
        return render(request,'Guest/login.html')
    

def registration(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        
        username = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        address = request.POST.get("addres")
        photo = request.FILES.get("photo")
        password = request.POST.get("password")
        ward_id = tbl_panchayathward.objects.get(id=request.POST.get("sel_ward"))

        tbl_reg.objects.create(user_name=username,
                               user_email=email,
                               user_contact=contact,
                               user_address=address,
                               user_password=password,
                               ward=ward_id,
                               user_photo=photo)
        return redirect('Guest:login')

    else:
        return render(request, 'Guest/registration.html', {"district":district})


def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

def ajaxpanchayath(request):
    panchayath=tbl_panchayath.objects.filter(place=request.GET.get("pid"))
    return render(request,'Guest/AjaxPanchayath.html',{'panchayath':panchayath})

def ajaxward(request):
    ward=tbl_panchayathward.objects.filter(panchayath=request.GET.get("pid"))
    return render(request,'Guest/Ajaxward.html',{'ward':ward})


def Panchayath(request):
    district = tbl_district.objects.all()
    if request.method =="POST":
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_panchayath.objects.create(panchayath_name=request.POST.get("name"),
            panchayath_email=request.POST.get("email"),
            panchayath_contact=request.POST.get("contact"),
            panchayath_address=request.POST.get("address"),
            place=place,
            panchayath_photo=request.FILES.get("photo"),
            panchayath_proof=request.FILES.get("proof"),
            panchayath_password=request.POST.get("password"))
        return redirect("Guest:login")
    else:
        return render(request,'Guest/Panchayath.html',{'district':district})

def Addpaliativecare(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        photo=request.FILES.get("photo")
        proof=request.FILES.get("photo")
        password=request.POST.get("name")
        panchayath_id = tbl_panchayath.objects.get(id=request.POST.get("sel_panchayath"))        
        tbl_paliativecare.objects.create(paliativecare_name=name,
                                        paliativecare_email=email,
                                        paliativecare_contact=contact,
                                        paliativecare_address=address,
                                        paliativecare_photo=photo,
                                        paliativecare_proof=proof,
                                        paliativecare_password=password,
                                        panchayath=panchayath_id,                                        
                                        )
        return render(request,'Guest/Addpaliativecare.html',{'msg':"Added"})
    else:
        return render(request,'Guest/Addpaliativecare.html',{'district':district})