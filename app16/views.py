from django.shortcuts import render
from django.shortcuts import redirect
from app16.models import UserModel
from app16.models import AdminModel
from app16.models import ProductModel
from django.contrib import messages


def showIndex(request):
    result = ProductModel.objects.all()
    if result:
        return render(request, "index.html", {"data": result})
    else:
        return render(request, "index.html", {"error": "Products are Not Available"})



def Usersite(request):
    return render(request,"usersite.html")


def usercreateAc(request):

    return render(request,"usercreateAc.html")


def UserAcSave(request):
    nm = request.POST.get("u1")
    dob = request.POST.get("u2")
    gen = request.POST.get("u3")
    mob = request.POST.get("u4")
    password = request.POST.get("u5")
    UserModel(name=nm,DOB=dob,Gender=gen,Mobile=mob,Password=password).save()
    messages.success(request, "Sucessfull Create Account...Thanku!!")
    return redirect('usercreateAc')


def userLogin(request):
    return render(request,"userLogin.html")


def UserLogin1(request):
    unm=request.POST.get("a1")
    upass=request.POST.get("a2")
    res=UserModel.objects.filter(name=unm,Password=upass)
    if res:
        return redirect ('main')
    else:
        messages.error(request,"Invalid User And Password")
        return redirect('userLogin')


def Adminsite(request):
    return render(request,"adminsite.html")


def AdmincreateAc(request):

    return render(request, "AdmincreateAc.html")


def AdminAcSave(request):
    nm = request.POST.get("A1")
    dob = request.POST.get("A2")
    gen = request.POST.get("A3")
    mob = request.POST.get("A4")
    password = request.POST.get("A5")
    AdminModel(name=nm, DOB=dob, Gender=gen, Mobile=mob, Password=password).save()
    messages.success(request, "Sucessfull Create Account...Thanku!!")
    return redirect('AdmincreateAc')


def AdminLogin(request):
    return render(request,"AdminLogin.html")


def AdminLogin1(request):
    unm=request.POST.get("p1")
    upass=request.POST.get("p2")
    res=AdminModel.objects.filter(name=unm,Password=upass)
    if res:
        return render (request,"Addproduct.html")
    else:
        messages.error(request,"Invalid Admin-Name And Password")
        return redirect('AdminLogin')


def save_product(request):
    nm=request.POST.get("p1")
    pr=request.POST.get("p2")
    qn=request.POST.get("p3")
    img=request.FILES["p4"]
    cate=request.POST.get("p5")
    ProductModel(name=nm,price=pr,quantity=qn,image=img,category=cate).save()
    messages.success(request, "Product is saved")
    return render(request,"Addproduct.html")


def AddtoCart(request):

    name=request.GET.get("name")
    price=request.GET.get("price")

    abc={"total_cookies":len(request.COOKIES)}

    response=render(request,"index.html",abc)

    response.set_cookie(key=price,value=name)
    return response


