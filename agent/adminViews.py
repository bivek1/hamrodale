from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddHouse, EditUserProfile, LandForm, RentForm, BusinessForm, EditAdminProfile, ImageForm
from .models import advertise, house, Customer, CustomUser, land, rent, business, requestBuy, comment, ImagesAd
from django.urls import reverse
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.core.files.storage import FileSystemStorage
def admin_page(request):
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    totalmember = Customer.objects.count()
    totaladvertise = advertise.objects.count()
    totalland = land.objects.count()
    totalhouse = house.objects.count()
    totalrent = rent.objects.count()
    totalbusiness = business.objects.count()
    totalreq = requestBuy.objects.count()
    comments = comment.objects.filter(unread = True).exclude(comment_by= request.user).order_by('-created_date')[:5]
    countcom = comment.objects.filter(unread = True).exclude(comment_by= request.user).count()
    dist = {
        'member': totalmember,
        'ads': totaladvertise,
        'house': totalhouse,
        'land':totalland,
        'rent': totalrent,
        'business': totalbusiness,  
        'req':totalreq,
        'comment': comments,
        'countcom':countcom,
        'visit': num_visits,
    }
    return render(request, "admin_templates/base_template.html", dist)

def total_ads(request):
    total = advertise.objects.all()
    return render(request, "admin_templates/total_ads.html", {'advertise': total})

def total_member(request):
    total = Customer.objects.all()
    return render(request, "admin_templates/total_member.html", {'mem': total})







# Normal Fucntionss.................

def update_profile(request):
    profile = CustomUser.objects.get(id = request.user.id)
    form = EditAdminProfile()
    form.fields['email'].initial = profile.email
    form.fields['first_name'].initial = profile.first_name
    form.fields['last_name'].initial = profile.last_name
    # form.fields['username'].initial = profile.username    
    return render(request, "admin_templates/update_profile.html", {'form':form})
    
def update_profile_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        form = EditAdminProfile(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            # username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user = CustomUser.objects.get(id = request.user.id)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            # user.username = username
            user.save()
            messages.success(request, "Sucessfully updated ads")
            return HttpResponseRedirect(reverse('update_profile_admin'))
        else:
            messages.error(request, "Failed to updates ads")
            return HttpResponseRedirect(reverse('update_profile_admin'))
  
def add_house(request):
    form = AddHouse()
    return render(request, "admin_templates/add_house.html", {'form': form})

def add_house_save(request):

    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
    
        form = AddHouse(request.POST, request.FILES)
        images = request.FILES.getlist("file[]")
        if form.is_valid():
            title = form.cleaned_data['title']
            district = form.cleaned_data['district']
            woda = form.cleaned_data['woda']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            price = form.cleaned_data['price']
            price_in_words = form.cleaned_data['price_in_words']
            selling_in = form.cleaned_data['selling_in']
            landsize = form.cleaned_data['landsize']
            floor = form.cleaned_data['floor']
            bedroom = form.cleaned_data['bedroom']
            bathroom = form.cleaned_data['bathroom']
            kitchen = form.cleaned_data['kitchen']
            roadsize = form.cleaned_data['roadsize']
            face_towards = form.cleaned_data['face_towards']
            garden = form.cleaned_data['garden']
            garage = form.cleaned_data['garage']
            undergroundtank = form.cleaned_data['undergroundtank']
            house_pic = form.cleaned_data['house_pic']
            # try: 
            house_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description = description,  images = house_pic )
            house_data.save()
            house_info = house(objectname = house_data, landsize= landsize, floor = floor, bedroom= bedroom, bathroom = bathroom, kitchen = kitchen,
                            face_toward = face_towards, road_size = roadsize, garden = garden, garage = garage, undergroudTank = undergroundtank)
            house_info.save()
            for img in images:
                fs = FileSystemStorage()
                file_path = fs.save(img.name, img)
                image = ImagesAd(post= house_data, image= file_path)
                image.save()
            messages.success(request, "Sucesssfully Inserted Your Ads")
            return HttpResponseRedirect(reverse('manage_ads_admin'))
            # except:
                # messages.error(request, "Failed to Insert Your Ads")
                # return render(request, "admin_templates/add_house.html", {'form': form})
                # return HttpResponseRedirect(reverse('add_house_admin')) 
        else:
            messages.error(request, "Failed to Insert Your Ads Try Again")
            return render(request, "admin_templates/add_house.html", {'form': form})

def add_land(request):
    form = LandForm()
    return render(request, "admin_templates/add_land.html", {'form': form})
 
def add_land_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
        form = LandForm(request.POST, request.FILES)
        images = request.FILES.getlist("file[]")
        if form.is_valid():
            title = form.cleaned_data['title']
            district = form.cleaned_data['district']
            woda = form.cleaned_data['woda']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            price = form.cleaned_data['price']
            price_in_words = form.cleaned_data['price_in_words']
            selling_in = form.cleaned_data['selling_in']
            landsize = form.cleaned_data['landsize']
            roadsize = form.cleaned_data['roadsize']
            electricity = form.cleaned_data['electricity']
            plotting = form.cleaned_data['plotting']
            land_pic = form.cleaned_data['land_pic']
            try: 
                land_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description = description, images = land_pic )
                land_data.save()
                house_info = land(objectname = land_data, landsize= landsize, road_size =roadsize, electrivityline = electricity, plotting = plotting)
                house_info.save()
                for img in images:
                    fs = FileSystemStorage()
                    file_path = fs.save(img.name, img)
                    image = ImagesAd(post= land_data, image= file_path)
                    image.save()
                messages.success(request, "Sucesssfully Inserted Your Ads")
                return HttpResponseRedirect(reverse('manage_ads_admin'))
            except:
                messages.error(request, "Failed to Insert Your Ads")
                return HttpResponseRedirect(reverse('add_house_admin')) 
        else:
            return HttpResponseRedirect(reverse('add_house_admin'))
        
def add_rent(request):
    form = RentForm()
    return render(request, "admin_templates/add_rent.html", {'form': form})

def add_rent_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
        form = RentForm(request.POST, request.FILES)
        images = request.FILES.getlist("file[]")
        if form.is_valid():
            title = form.cleaned_data['title']
            district = form.cleaned_data['district']
            woda = form.cleaned_data['woda']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            price = form.cleaned_data['price']
            price_in_words = form.cleaned_data['price_in_words']
            selling_in = form.cleaned_data['selling_in']
            rentroom = form.cleaned_data['rentroom']
            bathroom = form.cleaned_data['bathroom']
            internet = form.cleaned_data['internet']
            garage = form.cleaned_data['garage']
            tvchannel = form.cleaned_data['tvchannel']
            rent_pic = form.cleaned_data['rent_pic']
            # try: 
            rent_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description= description, images = rent_pic )
            rent_data.save()
            rent_info = rent(objectname = rent_data, rentroom= rentroom, bathroom = bathroom, internet = internet, garage = garage, tvchannel = tvchannel)
            rent_info.save()
            for img in images:
                fs = FileSystemStorage()
                file_path = fs.save(img.name, img)
                image = ImagesAd(post= rent_data, image= file_path)
                image.save()
            messages.success(request, "Sucesssfully Inserted Your Ads")
            return HttpResponseRedirect(reverse('manage_ads_admin'))
            # except:
            #     messages.error(request, "Failed to Insert Your Ads")
            #     return HttpResponseRedirect(reverse('add_rent_admin')) 
        else:
            return HttpResponseRedirect(reverse('add_rent_admin'))


def add_business(request):
    form = BusinessForm()
    return render(request, "admin_templates/add_business.html", {'form': form})

def add_business_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
        form = BusinessForm(request.POST, request.FILES)
        images = request.FILES.getlist("file[]")
        if form.is_valid():
            title = form.cleaned_data['title']
            district = form.cleaned_data['district']
            woda = form.cleaned_data['woda']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            price = form.cleaned_data['price']
            price_in_words = form.cleaned_data['price_in_words']
            selling_in = form.cleaned_data['selling_in']
            businessType = form.cleaned_data['business']
            business_pic = form.cleaned_data['business_pic']
            # try: 
            business_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description= description, images = business_pic )
            business_data.save()
            rent_info = business(objectname = business_data, businesstype = businessType)
            rent_info.save()
            for img in images:
                fs = FileSystemStorage()
                file_path = fs.save(img.name, img)
                image = ImagesAd(post= business_data, image= file_path)
                image.save()
            messages.success(request, "Sucesssfully Inserted Your Ads")
            return HttpResponseRedirect(reverse('manage_ads_admin'))
            
        else:
            messages.error(request, "Failed to Insert Your Ads")
            return render(request, "admin_templates/add_business.html", {'form': form})
   

def manage_ads(request):
    user_ads = advertise.objects.filter(created_by = request.user)
    dist = {
        'advertise': user_ads,
        }
    return render(request, "admin_templates/manage_ads.html", dist)    

def delete_ads(request, id):
    del_ads = advertise.objects.get(id = id)
    del_ads.delete()
    messages.success(request, "Your ads has been deleted")
    return HttpResponseRedirect(reverse('manage_ads_admin'))

def edit_ads(request, edit_id):
    request.session['edit_id'] = edit_id
    edit_ads = advertise.objects.get(id = edit_id)
    try:
        ads = house.objects.get(objectname = edit_ads)
        form = AddHouse()
        form.fields['title'].initial = edit_ads.title
        form.fields['district'].initial = edit_ads.district
        form.fields['woda'].initial = edit_ads.woda
        form.fields['description'].initial = edit_ads.description
        form.fields['location'].initial = edit_ads.location
        form.fields['price'].initial = edit_ads.price
        form.fields['price_in_words'].initial = edit_ads.price_in_words
        form.fields['selling_in'].initial = edit_ads.selling_in
        form.fields['landsize'].initial = edit_ads.house.landsize
        form.fields['roadsize'].initial = edit_ads.house.road_size
        form.fields['floor'].initial = edit_ads.house.floor
        form.fields['bedroom'].initial = edit_ads.house.bedroom
        form.fields['bathroom'].initial = edit_ads.house.bathroom
        form.fields['kitchen'].initial = edit_ads.house.kitchen
        form.fields['face_towards'].initial = edit_ads.house.face_toward
        form.fields['garden'].initial = edit_ads.house.garden
        form.fields['garage'].initial = edit_ads.house.garage
        form.fields['undergroundtank'].initial = edit_ads.house.undergroudTank
        form.fields['house_pic'].initial = edit_ads.images.url
      
    except:
        pass
    try: 
        ads = land.objects.get(objectname = edit_ads)
        form = LandForm()
        form.fields['title'].initial = edit_ads.title
        form.fields['district'].initial = edit_ads.district
        form.fields['woda'].initial = edit_ads.woda
        form.fields['description'].initial = edit_ads.description
        form.fields['location'].initial = edit_ads.location
        form.fields['price'].initial = edit_ads.price
        form.fields['price_in_words'].initial = edit_ads.price_in_words
        form.fields['landsize'].initial = edit_ads.land.landsize
        form.fields['roadsize'].initial = edit_ads.land.road_size
        form.fields['electricity'].initial = edit_ads.land.electrivityline
        form.fields['plotting'].initial = edit_ads.land.plotting
    except:
        pass
    try:
        ads = rent.objects.get(objectname = edit_ads)
        form = RentForm()
        form.fields['title'].initial = edit_ads.title
        form.fields['district'].initial = edit_ads.district
        form.fields['woda'].initial = edit_ads.woda
        form.fields['description'].initial = edit_ads.description
        form.fields['location'].initial = edit_ads.location
        form.fields['price'].initial = edit_ads.price
        form.fields['price_in_words'].initial = edit_ads.price_in_words
        form.fields['selling_in'].initial = edit_ads.selling_in
        form.fields['rentroom'].initial = edit_ads.land.rentroom
        form.fields['bathroom'].initial = edit_ads.land.bathroom
        form.fields['internet'].initial = edit_ads.land.internet
        form.fields['garage'].initial = edit_ads.land.garage
        form.fields['tvchannel'].initial = edit_ads.land.tvchannel

    except:
        pass
    try: 
        ads = business.objects.get(objectname = edit_ads)
        form = BusinessForm()
        form.fields['title'].initial = edit_ads.title
        form.fields['district'].initial = edit_ads.district
        form.fields['woda'].initial = edit_ads.woda
        form.fields['description'].initial = edit_ads.description
        form.fields['location'].initial = edit_ads.location
        form.fields['price'].initial = edit_ads.price
        form.fields['price_in_words'].initial = edit_ads.price_in_words
        form.fields['selling_in'].initial = edit_ads.selling_in
        form.fields['business'].initial = edit_ads.business.businesstype
    except:
        pass
    
    return render(request, "admin_templates/edit_ads.html" ,{'form':form,'id':edit_id})

def edit_ads_save(request):
    if request.method != "POST":
        return HttpResponse("<h1>Method not Allowed</h1>")
    else:
        edit_id = request.session.get('edit_id')
        if edit_id == None:
            return HttpResponseRedirect(reverse('manage_ads_admin'))
        else:
            try:
                ads = house.objects.get(objectname = edit_id)
                form = AddHouse(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    district = form.cleaned_data['district']
                    woda = form.cleaned_data['woda']
                    description = form.cleaned_data['description']
                    location = form.cleaned_data['location']
                    price = form.cleaned_data['price']
                    price_in_words = form.cleaned_data['price_in_words']
                    selling_in = form.cleaned_data['selling_in']
                    landsize = form.cleaned_data['landsize']
                    floor = form.cleaned_data['floor']
                    bedroom = form.cleaned_data['bedroom']
                    bathroom = form.cleaned_data['bathroom']
                    kitchen = form.cleaned_data['kitchen']
                    roadsize = form.cleaned_data['roadsize']
                    face_towards = form.cleaned_data['face_towards']
                    garden = form.cleaned_data['garden']
                    garage = form.cleaned_data['garage']
                    undergroundtank = form.cleaned_data['undergroundtank']
                    house_pic = request.FILES['house_pic']
                else:
                    return render(request, 'admin_templates/edit_ads.html', {'form':form})
                try: 
                    ads_data = advertise.objects.get(id = edit_id)
                    ads_data.title = title
                    ads_data.district = district
                    ads_data.woda =  woda
                    ads_data.description =  description
                    ads_data.location = location
                    ads_data.price = price
                    ads_data.price_in_words = price_in_words
                    ads_data.selling_in = selling_in
                    ads_data.images = house_pic
                    house_data = house.objects.get(objectname = edit_id)
                    house_data.landsize = landsize
                    house_data.floor = floor
                    house_data.bedroom = bedroom
                    house_data.bathroom = bathroom
                    house_data.kitchen = kitchen
                    house_data.road_size = roadsize
                    house_data.face_toward = face_towards
                    house_data.garden = garden
                    house_data.garage = garage
                    house_data.undergroudTank = undergroundtank
                    ads_data.save()
                    house_data.save()
                    del request.session['edit_id']
                    messages.success(request, "Sucesssfully updated Your Ads")
                    return HttpResponseRedirect(reverse('manage_ads_admin'))
                except:
                    messages.error(request, "Failed to Update Your Ads")
                    
                                 
            except:
                pass
            try:
                ads = land.objects.get(objectname = edit_id)
                form = LandForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    district = form.cleaned_data['district']
                    woda = form.cleaned_data['woda']
                    description = form.cleaned_data['description']
                    location = form.cleaned_data['location']
                    price = form.cleaned_data['price']
                    price_in_words = form.cleaned_data['price_in_words']
                    selling_in = form.cleaned_data['selling_in']
                    landsize = form.cleaned_data['landsize']
                    roadsize = form.cleaned_data['roadsize']
                    electricity = form.cleaned_data['electricity']
                    plotting = form.cleaned_data['plotting']
                    land_pic = request.FILES['land_pic']
                    try: 
                        ads_data = advertise.objects.get(id = edit_id)
                        ads_data.title = title
                        ads_data.district = district
                        ads_data.woda =  woda
                        ads_data.description =  description
                        ads_data.location = location
                        ads_data.price = price
                        ads_data.price_in_words = price_in_words
                        ads_data.selling_in = selling_in
                        ads_data.images = land_pic
                        land_data = land.objects.get(objectname = edit_id)
                        land_data.landsize = landsize
                        land_data.road_size = roadsize
                        land_data.electrivityline = electricity
                        land_data.plotting = plotting
                        ads_data.save()
                        land_data.save()
                        del request.session['edit_id']
                        messages.success(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('manage_ads_admin'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads_admin'))
                else:
                    return render(request, 'admin_templates/edit_ads.html', {'form':form})
            except:
                pass
            try:
                ads = business.objects.get(objectname = edit_id)
                form = BusinessForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    district = form.cleaned_data['district']
                    woda = form.cleaned_data['woda']
                    description = form.cleaned_data['description'] 
                    location = form.cleaned_data['location']
                    price = form.cleaned_data['price']
                    price_in_words = form.cleaned_data['price_in_words']
                    selling_in = form.cleaned_data['selling_in']
                    businesses = form.cleaned_data['business']
                    business_picture = request.FILES['business_pic']
                    
                    try:
                        ads_data = advertise.objects.get(id = edit_id)
                        ads_data.title = title
                        ads_data.district = district
                        ads_data.woda =  woda
                        ads_data.description =  description
                        ads_data.location = location
                        ads_data.price = price
                        ads_data.price_in_words = price_in_words
                        ads_data.selling_in = selling_in
                        ads_data.images = business_picture
                        business_data = business.objects.get(objectname = edit_id)
                        business_data.businesstype = businesses
                        ads_data.save()
                        business_data.save()
                        del request.session['edit_id']
                        messages.success(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('manage_ads_admin'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads_admin'))
                else:
                    return render(request, 'admin_templates/edit_ads.html', {'form':form})
            except:
                pass
            try:
                ads = rent.objects.get(objectname = edit_id)
                form = RentForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    district = form.cleaned_data['district']
                    woda = form.cleaned_data['woda']
                    description = form.cleaned_data['description']
                    location = form.cleaned_data['location']
                    price = form.cleaned_data['price']
                    price_in_words = form.cleaned_data['price_in_words']
                    selling_in = form.cleaned_data['selling_in']
                    rentroom = form.cleaned_data['rentroom']
                    bathroom = form.cleaned_data['bathroom']
                    internet = form.cleaned_data['internet']
                    garage = form.cleaned_data['garage']
                    tvchannel = form.cleaned_data['tvchannel']
                    rent_pic = request.FILES['rent_pic']
                    
                    try:
                        ads_data = advertise.objects.get(id = edit_id)
                        ads_data.title = title
                        ads_data.district = district
                        ads_data.woda =  woda
                        ads_data.description =  description
                        ads_data.location = location
                        ads_data.price = price
                        ads_data.price_in_words = price_in_words
                        ads_data.selling_in = selling_in
                        ads_data.images = rent_pic
                        rent_data = rent.objects.get(objectname = edit_id)
                        rent_data.rentroom = rentroom
                        rent_data.bathroom = bathroom
                        rent_data.internet = internet
                        rent_data.garage = garage
                        rent_data.tvchannel = tvchannel
                        ads_data.save()
                        rent_data.save()
                        del request.session['edit_id']
                        messages.success(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('manage_ads_admin'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads_admin'))
                else:
                    return render(request, 'admin_templates/edit_ads.html', {'form':form})
            except:
                pass
        return HttpResponseRedirect(reverse('manage_ads_admin'))
        
def requested(request):
    reqads = requestBuy.objects.all()
    return render(request, "admin_templates/requestads.html", {'reqads':reqads})

def premium_ads(request):
    adver = advertise.objects.all()
    if request.method == 'POST':
        ads_id = request.POST['ads_id']
        ads = advertise.objects.get(id = ads_id)
        ads.premium = 'Yes'
        ads.save()
        messages.success(request, "Added to premium list")
        return HttpResponseRedirect(reverse('premium')) 
    return render(request, "admin_templates/premium_ads.html", {'ads':adver})


def features_ads(request):
    adver = advertise.objects.all()
    if request.method == 'POST':
        ads_id = request.POST['ads_id']
        ads = advertise.objects.get(id = ads_id)
        ads.feature = 'Yes'
        ads.save()
        messages.success(request, "Added to features list")
        return HttpResponseRedirect(reverse('features')) 
    return render(request, "admin_templates/features_ads.html", {'ads':adver})


def remove_premium(request, ads_id):
    ads = advertise.objects.get(id = ads_id)
    ads.premium = 'No'
    ads.save()
    messages.success(request, "Sucessfully removed from premium")
    return HttpResponseRedirect(reverse('premium')) 

def remove_feature(request, ads_id):
    ads = advertise.objects.get(id = ads_id)
    ads.feature = 'No'
    ads.save()
    messages.success(request, "Sucessfully removed from features")
    return HttpResponseRedirect(reverse('features')) 

def add_dealed(request, ad_id):
    ads = requestBuy.objects.get(id = ad_id)
    ads.dealed = 'Yes'
    ads.save()
    return HttpResponseRedirect(reverse('requestads'))
    
    
def notification(request):
    allcom = comment.objects.all().order_by("-created_date")
   
    allc = comment.objects.filter(unread = True)
    for com in allc:
        com.unread = False
        com.save()
    return render(request, "admin_templates/notification.html", {'all':allcom})
