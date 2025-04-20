from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from User.models import*



def largest(request):
    return render(request,'Admin/Largest.html')

def add(request):
    if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("number2"))
        c=a+b
        return render(request,"Admin/Add.html",{'result':c})
    else:
        return render(request,"Admin/Add.html")
    
def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("number2"))

        if a>b:
            return render(request,"Admin/Largest.html",{'result':a})
        else:
            return render(request,"Admin/Largest.html",{'result':b})

    else:
        return render(request,"Admin/Largest.html")
    
def calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("Number1"))
        b=int(request.POST.get("number2"))
        btn=request.POST.get("")
        if btn=='+':
            return render(request,"Admin/Largest.html",{'result':btn})
        elif btn=='*':
            return render(request,"Admin/Largest.html",{'result':b})
        elif btn=='*':
            return render(request,"Admin/Largest.html",{'result':b})
    else:
        return render(request,"Admin/Calculator.html")

#----------------------------------------------------------------------------


def homepage(request):
    return render(request,'Admin/Homepage.html')

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
       district=request.POST.get("district")
       tbl_district.objects.create(district_name=district)
       return render(request,'Admin/District.html',{'dis':dis})
    else:
        return render(request,'Admin/District.html',{'dis':dis})
    
def category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get('category')
        tbl_category.objects.create(category_name=category) 
        return render(request,'Admin/Category.html',{'cate':cat})
    else:
        return render(request,'Admin/Category.html',{'cate':cat}) 

def adminreg(request):
    admin=tbl_Adminreg.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        tbl_Adminreg.objects.create(adminreg_name=name,adminreg_email=email,adminreg_password=password)
        return render(request,'Admin/adminreg.html',{'reg':admin})
    else:
        return render(request,'Admin/adminreg.html',{'reg':admin}) 
    
def deladmin(request,id):
    tbl_Adminreg.objects.get(id=id).delete()  
    return redirect("Admin:Adminreg")

def place(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
         dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
         tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
         return redirect("Admin:place")
    else:
         return render(request,'Admin/place.html',{'result':dis,'r':place})
def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")
def editplace(request,id):
    p=tbl_place.objects.get(id=id)
    p1=tbl_place.objects.all()   
    if request.method=="POST":
        p.place_name=request.POST.get("place_name")
        p.save()
        return redirect("Admin:place")
    else:
        return render(request,'Admin/place.html',{'rr':p,'r':p1})
def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")

def eddistrict(request,id):
    district=tbl_district.objects.get(id=id)    
    if request.method=="POST":
        district.district_name=request.POST.get("district")
        district.save()
        return redirect("Admin:district")
    else: 
        return render(request,'Admin/District.html',{'d':district})   
def Viewpanchayath(request):
    use=tbl_panchayath.objects.filter(panchayath_status=0)
    accept=tbl_panchayath.objects.filter(panchayath_status=1)
    reject=tbl_panchayath.objects.filter(panchayath_status=2)
    return render(request,'Admin/Viewpanchayath.html',{'result':use,'accept':accept,'reject':reject})  

def viewpanchayathaccept(request,id):
    data=tbl_panchayath.objects.get(id=id)
    data.panchayath_status=1
    data.save()
    return render(request,'Admin/Viewpanchayath.html',{'msg':"Accepted"})

def viewpanchayathreject(request,id):
    data=tbl_panchayath.objects.get(id=id)
    data.panchayath_status=2
    data.save()
    return render(request,'Admin/Viewpanchayath.html',{'msg':"Rejected"})

def ward(request):
    ward=tbl_ward.objects.all()
    if request.method=="POST":
       
       tbl_ward.objects.create(ward_number=request.POST.get("number"))
       return redirect('Admin:ward')
    else:
        return render(request,'Admin/ward.html',{'ward':ward})
    
def delward(request,id):
    tbl_ward.objects.get(id=id).delete()
    return redirect("Admin:ward")    

def addpaliativecaredelete(request,id):
    tbl_paliativecare.objects.get(id=id).delete()
    return redirect("Admin:Addpaliativecare")

def viewcomplaint(request):
    complaint=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,'Admin/Viewcomplaint.html',{'complaint':complaint})

def replyedcomplaint(request):
    complaint=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/Replyedcomplaint.html',{'complaint':complaint})

def replycomplaint(request,id):
    b=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        b.complaint_reply=request.POST.get("txt_reply")
        b.complaint_status=1
        b.save()
        return redirect("Admin:viewcomplaint")
    else:
        return render(request,'Admin/Reply.html')

def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")