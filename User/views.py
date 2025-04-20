from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# from django.db.models import Sum
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    return render(request,"User/Homepage.html")
def profile(request):
    user=tbl_reg.objects.get(id=request.session["uid"])
    return render(request,'User/Myprofile.html',{'user':user})

def editprofile(request):
     b=tbl_reg.objects.get(id=request.session["uid"])
     if request.method=="POST":
        b.user_name=request.POST.get("name")
        b.user_email=request.POST.get("email")
        b.user_contact=request.POST.get("contact")
        b.user_address=request.POST.get("address")
        b.save()
        return redirect("User:profile")
     else:
         return render(request,"User/EditProfile.html",{'user':b})
     
def changepassword(request):
     b=tbl_reg.objects.get(id=request.session["uid"])
     olda=b.user_password
     oldb=request.POST.get("user_old_password")
     new=request.POST.get("user_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.user_password=request.POST.get("user_new_password")
                b.save()
                return render(request,"User/Myprofile.html",{"msg":"Password Changed"})
            else:
                return render(request,"User/Changepassword.html",{"msg":"New Password not matched"})
        else:
            return render(request,"User/Changepassword.html",{"msg":"Old Password not matched"})
     else:
         return render(request,"User/Changepassword.html")  


def addpatient(request):
    patient=tbl_patient.objects.filter(user=request.session["uid"])
    if request.method == "POST":
        
        tbl_patient.objects.create(
            patient_name=request.POST.get("name"),
            patient_age=request.POST.get("age"),
            patient_height=request.POST.get("height"),
            patient_weight=request.POST.get("weight"),
            patient_gender=request.POST.get("gender"),
            patient_description=request.POST.get("description"),
            user=tbl_reg.objects.get(id=request.session["uid"])
            )
        return render(request, 'User/addpatient.html',{'patient':patient})  
    else:
        
        return render(request, 'User/addpatient.html',{'patient':patient})  
    

   
def myrequest(request):
    req=tbl_request.objects.filter(patient_id__user=request.session['uid'])
    return render(request,"User/myrequest.html",{'result':req})


def viewpaliativecare(request,pid):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    use=tbl_paliativecare.objects.filter(paliativecare_status=1)
    for i in use:
        tot=0
        ratecount=tbl_rating.objects.filter(paliativecare_id=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(paliativecare_id=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(use,parry)
    return render(request,"User/ViewPaliativecare.html",{'result':datas,"pid":pid,"ar":ar})

def sendrequest(request,pid,plid):
    if request.method == "POST":
        tbl_request.objects.create(
            request_fromdate=request.POST.get("from"),
            request_todate=request.POST.get("to"),
            request_description=request.POST.get("text"),
            patient_id=tbl_patient.objects.get(id=plid),
            paliativecare_id=tbl_paliativecare.objects.get(id=pid),
        )
        return redirect("User:mybooking")
    else:
        return render(request, "User/Sendrequest.html")
    
def complaint(request):
    complaint = tbl_complaint.objects.filter(user=request.session['uid'])
    if request.method=='POST':
        title=request.POST.get('txt_title')
        content=request.POST.get('text_content')
        userid=tbl_reg.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userid)
        return redirect('User:complaint')
    else:
        return render(request,"User/Complaint.html",{'complaint':complaint})



def mybooking(request):
    book = tbl_request.objects.filter(patient_id__user=request.session["uid"])
    return render(request,"User/MyBooking.html",{"book":book})

#payment

def payment(request,id):
   data = tbl_request.objects.get(id=id)
   amount = data.request_amount
   amount=int(amount)
   if request.method == "POST":
      data.request_status = 3
      data.save()
      return redirect("User:loader")
   else:
      return render(request,"User/Payment.html", {"total":amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

#rating

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(paliativecare_id=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(paliativecare_id=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')

    user_review=request.GET.get('user_review')

    pid=request.GET.get('pid')

    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user_review=user_review,rating_data=rating_data,paliativecare_id=tbl_paliativecare.objects.get(id=pid),user_id=tbl_reg.objects.get(id=request.session['uid']))
    stardata=tbl_rating.objects.filter(paliativecare_id=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(paliativecare_id=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(paliativecare_id=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")