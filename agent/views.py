from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import CustomerForm
from .models import CustomUser, Customer, house, rent, land, business, advertise, comment, requestBuy, ImagesAd

# Create your views here.
def homepage(request):
    houses = house.objects.all()[0:6]
    lands = land.objects.all()[0:6]
    rents = rent.objects.all()[0:6]
    businesses = business.objects.all()[0:6]
    premium = advertise.objects.filter(premium = 'Yes')[0:6]
    feature = advertise.objects.filter(feature = 'Yes')[0:6]
    
    dist = {
        'house':houses,
        'land': lands,
        'rent': rents,
        'business': businesses,
        'premium': premium,
        'feature': feature,
    }
    return render(request, "base_templates/index.html", dist)
def search(request):
    
    query = request.GET['searchlocation']
    try:
        search_result = advertise.objects.filter(location__icontains = query)
        search_title = advertise.objects.filter(title__icontains = query)
        messages.success(request, "Showing you ads which includes " +"'"+query+"'")
    except:
        messages.error(request, "Sorry no result found which includes " +"'"+query+"'")
    return render(request, "base_templates/search.html", {'loc':search_result, 'title':search_title})

def searchads(request):
    opt = request.GET['options']
    pricerang = int(request.GET['pricerange'])
    location = request.GET['location']

    try:
        if opt == 'house':
            ox = 'house'
            print("house choosen")
            if pricerang == 99999:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 99999))
            elif pricerang == 999999:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 999999 ))
            elif pricerang == 4999999:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 4999999 ))
            elif pricerang == 9999999:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 9999999 ))
            elif pricerang == 29999999:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 29999999 ))
            else:
                realads = house.objects.filter(objectname__district = location).filter(objectname__price__gt= 49999999)
        elif opt == 'land':
            ox = 'land'
            print("Land choosen")
            if pricerang == 99999:
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 99999))
            elif pricerang == 999999:
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__range = (99999, 999999 ))
            elif pricerang == 4999999:
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__range = (999999, 4999999 ))
            elif pricerang == 9999999:
                print('onecore')
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__range = (4999999, 9999999 ))
            elif pricerang == 29999999:
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__range = (9999999, 29999999 ))
            else:
                realads = land.objects.filter(objectname__district = location).filter(objectname__price__gt= 49999999)
        elif opt == 'business':
            ox = 'business'
            if pricerang == 99999:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 99999))
            elif pricerang == 999999:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__range = (99999, 999999 ))
            elif pricerang == 4999999:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__range = (999999, 4999999 ))
            elif pricerang == 9999999:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__range = (4999999, 9999999 ))
            elif pricerang == 29999999:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__range = (9999999, 29999999 ))
            else:
                realads = business.objects.filter(objectname__district = location).filter(objectname__price__gt= 49999999)
        else:
            ox = 'rent'
            if pricerang == 99999:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__range = (0, 99999))
            elif pricerang == 999999:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__range = (99999, 999999 ))
            elif pricerang == 4999999:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__range = (999999, 4999999 ))
            elif pricerang == 9999999:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__range = (4999999, 9999999 ))
            elif pricerang == 29999999:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__range = (9999999, 29999999 ))
            else:
                realads = rent.objects.filter(objectname__district = location).filter(objectname__price__gt= 49999999)
        return render(request, 'base_templates/searchads.html', {'ads':realads,'opt':opt})
    except:
        messages.error(request, "Sorry No Result Found")

    return render(request, "base_templates/searchads.html")


def loginpage(request):
    return render(request, "base_templates/login_page.html")

def dologin(request):
    if request.method != 'POST':
        return HttpResponse("<h1>This method is not allowed !</h1>")
    else:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user!= None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_page"))
            else:
                return HttpResponseRedirect(reverse("customer_page"))
        else:
            messages.error(request, "Invalid Login Credential")
            return HttpResponseRedirect(reverse('login'))
def register(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            # username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            number = form.cleaned_data['number']            
            try:
                user = CustomUser.objects.create_user(username=email, first_name= first_name, last_name=last_name, password=password, email = email, user_type = 2)

                user.customer.address = address
                user.customer.number = number
                user.save()
                messages.success(request, "Sucessfully Registered! Please Login Now!")
                return HttpResponseRedirect(reverse('login'))
            except:
                messages.error(request, "Email Already exist")
                return HttpResponseRedirect(reverse('register')) 
    
    else:
        return render(request, "base_templates/register.html", {'form':form})
        


def house_page(request):
    ads = house.objects.all()
    return render(request, "base_templates/house.html", {'ads':ads})


def land_page(request):
    ads = land.objects.all()
    return render(request, "base_templates/land.html", {'ads':ads})

def rent_page(request):
    ads = rent.objects.all()
    return render(request, "base_templates/rent.html", {'ads':ads})

def business_page(request):
    ads = business.objects.all()
    return render(request, "base_templates/business.html", {'ads':ads})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def details(request, ads_id):
    ads = advertise.objects.get(id = ads_id)
    request.session['curent_ads'] = ads_id
    req = False
    own_ads = False
    rest = requestBuy.objects.filter(req_ads = ads)
    extra = ImagesAd.objects.filter(post = ads_id)

    for res in rest:
        if res.req_by == request.user and res.req_ads == ads:
            req = True
        if ads.created_by == request.user:
            own_ads = True
    try:
        comments = comment.objects.filter(comment_ads = ads).order_by('-created_date')
        for com in comments:
            if com.comment_ads.created_by == request.user:
                com.ureadCustomer = False
                com.save()
    except:
        pass
    
    try:
        ads_mode = house.objects.get(objectname = ads_id)
        house_a = str(ads_mode.objectname.location)
        print(house_a)
        house_ad = house.objects.filter(objectname__location__icontains = house_a)
        house_ads = house_ad.exclude(objectname = ads_id)
    except:
        pass
    try:
        ads_mode = land.objects.get(objectname = ads_id)
        house_a = str(ads_mode.objectname.location)
        print(house_a)
        house_ad = land.objects.filter(objectname__location__icontains = house_a)
        house_ads = house_ad.exclude(objectname = ads_id)
    except:
        pass
    try:
        ads_mode = rent.objects.get(objectname = ads_id)
        house_a = str(ads_mode.objectname.location)
        print(house_a)
        house_ad = rent.objects.filter(objectname__location__icontains = house_a)
        house_ads = house_ad.exclude(objectname = ads_id)
    except:
        pass
    try:
        ads_mode = business.objects.get(objectname = ads_id)
        house_a = str(ads_mode.objectname.location)
        types = str(ads_mode.businesstype)
        print(house_a)
        house_ad = business.objects.filter(objectname__location__icontains = house_a).filter(businesstype = types)
        house_ads = house_ad.exclude(objectname = ads_id)
    except:
        pass
    if request.method == 'POST':
        if request.user.is_authenticated:
            com = request.POST['comment']
            save_com = comment(comment_ads = ads, comment_by= request.user, body = com)
            save_com.save()
            return render(request, "base_templates/details.html",{'ads':ads, 'house_ads':house_ads, 'comment':comments, 'req':req, 'own_ads':own_ads, 'extra':extra})
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "base_templates/details.html",{'ads':ads, 'house_ads':house_ads, 'comment':comments, 'req':req, 'own_ads':own_ads, 'extra':extra})    
    
def delete_cmt(request, cmt_id):
    ads_id = comment.objects.get(id = cmt_id)
    ads = request.session.get('curent_ads')
    ads_id.delete()
    return HttpResponseRedirect(reverse('details_page', kwargs= {'ads_id':ads})) 


def requestads(request, ads_id):
    ads_now = advertise.objects.get(id = ads_id)
    save_com = requestBuy(req_ads = ads_now, req_by = request.user)
    ads = request.session.get('curent_ads')
    save_com.save()
    
    messages.success(request, 'You request has been sent to our agents')
    
    return HttpResponseRedirect(reverse('details_page', kwargs= {'ads_id':ads}))

def premium_list(request):
    ads = advertise.objects.filter(premium = 'Yes')
    return render(request, "base_templates/premium.html", {'ads':ads})
def feature_list(request):
    ads = advertise.objects.filter(feature = 'Yes')
    return render(request, "base_templates/features.html", {'ads':ads})
    
    
   