from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddHouse, EditUserProfile, LandForm, RentForm, BusinessForm
from .models import advertise, house, Customer, CustomUser, land, rent, business, comment
from django.urls import reverse
from django.contrib import messages

def customer_page(request):
    profile_id = request.user
    comments = comment.objects.filter(comment_ads__created_by = request.user).filter(ureadCustomer = True).exclude(comment_by= request.user).order_by('-created_date')[:5]
    countcom = comment.objects.filter(comment_ads__created_by = request.user).filter(ureadCustomer = True).exclude(comment_by= request.user).count()
    return render(request, "customer_templates/base_template.html",{'countcom':countcom, 'comment': comments})

def update_profile(request):
    profile = Customer.objects.get(admin = request.user.id)
    form = EditUserProfile()
    form.fields['email'].initial = profile.admin.email
    form.fields['first_name'].initial = profile.admin.first_name
    form.fields['last_name'].initial = profile.admin.last_name
    # form.fields['username'].initial = profile.admin.username
    form.fields['address'].initial = profile.address
    form.fields['number'].initial = profile.number
    form.fields['profile_pic'].initial = profile.profile_pic
    
    return render(request, "customer_templates/update_profile.html", {'form':form})
    
def update_profile_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        form = EditUserProfile(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            print(first_name)
            last_name = form.cleaned_data["last_name"]
            # username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            number = form.cleaned_data['number']
            profile = form.cleaned_data['profile_pic']
            customer_model = Customer.objects.get(admin = request.user.id)
            customer_model.profile_pic = profile
            customer_model.address = address
            customer_model.number = number
            user = CustomUser.objects.get(id = request.user.id)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            # user.username = username
            user.save()
            customer_model.save()
            messages.success(request, "Sucessfully updated ads")
            return HttpResponseRedirect(reverse('update_profile'))
        else:
            messages.error(request, "Failed to updates ads")
            return HttpResponseRedirect(reverse('update_profile'))
  
def add_house(request):
    form = AddHouse()
    return render(request, "customer_templates/add_house.html", {'form': form})

def add_house_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
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
            house_pic = form.cleaned_data['house_pic']
            try: 
                house_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description = description,  images = house_pic )
                house_data.save()
                house_info = house(objectname = house_data, landsize= landsize, floor = floor, bedroom= bedroom, bathroom = bathroom, kitchen = kitchen,
                                face_toward = face_towards, road_size = roadsize, garden = garden, garage = garage, undergroudTank = undergroundtank)
                house_info.save()
                messages.success(request, "Sucesssfully Inserted Your Ads")
                return HttpResponseRedirect(reverse('manage_ads'))
            except:
                messages.error(request, "Failed to Insert Your Ads")
                return HttpResponseRedirect(reverse('add_house')) 
        else:
            return HttpResponseRedirect(reverse('add_house'))

def add_land(request):
    form = LandForm()
    return render(request, "customer_templates/add_land.html", {'form': form})
 
def add_land_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
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
            land_pic = form.cleaned_data['land_pic']
            try: 
                land_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description = description, images = land_pic )
                land_data.save()
                house_info = land(objectname = land_data, landsize= landsize, road_size =roadsize, electrivityline = electricity, plotting = plotting)
                house_info.save()
                messages.success(request, "Sucesssfully Inserted Your Ads")
                return HttpResponseRedirect(reverse('manage_ads'))
            except:
                messages.error(request, "Failed to Insert Your Ads")
                return HttpResponseRedirect(reverse('add_house')) 
        else:
            return HttpResponseRedirect(reverse('add_house'))
        
def add_rent(request):
    form = RentForm()
    return render(request, "customer_templates/add_rent.html", {'form': form})

def add_rent_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
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
            rent_pic = form.cleaned_data['rent_pic']
            try: 
                rent_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description= description, images = rent_pic )
                rent_data.save()
                rent_info = rent(objectname = rent_data, rentroom= rentroom, bathroom = bathroom, internet = internet, garage = garage, tvchannel = tvchannel)
                rent_info.save()
                messages.success(request, "Sucesssfully Inserted Your Ads")
                return HttpResponseRedirect(reverse('manage_ads'))
            except:
                messages.error(request, "Failed to Insert Your Ads")
                return HttpResponseRedirect(reverse('add_rent')) 
        else:
            return HttpResponseRedirect(reverse('add_rent'))
        


def add_business(request):
    form = BusinessForm()
    return render(request, "customer_templates/add_business.html", {'form': form})

def add_business_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>")
    else:
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
            businessType = form.cleaned_data['business']
            business_pic = form.cleaned_data['business_pic']
            try: 
                business_data = advertise(created_by = request.user, title =  title, district = district, woda = woda, location = location, price = price, price_in_words = price_in_words, selling_in = selling_in, description= description, images = business_pic )
                business_data.save()
                rent_info = business(objectname = business_data, businesstype = businessType)
                rent_info.save()
                messages.success(request, "Sucesssfully Inserted Your Ads")
                return HttpResponseRedirect(reverse('manage_ads'))
            except:
                messages.error(request, "Failed to Insert Your Ads")
                return HttpResponseRedirect(reverse('add_business')) 
        else:
            return HttpResponseRedirect(reverse('add_business'))

def manage_ads(request):
    user_ads = advertise.objects.filter(created_by = request.user)
    dist = {
        'advertise': user_ads,
        }
    return render(request, "customer_templates/manage_ads.html", dist)    

def delete_ads(request, id):
    del_ads = advertise.objects.get(id = id)
    del_ads.delete()
    messages.success(request, "Your ads has been deleted")
    return render(request, "customer_templates/manage_ads.html")

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
    
    return render(request, "customer_templates/edit_ads.html" ,{'form':form,'id':edit_id})

def edit_ads_save(request):
    if request.method != "POST":
        return HttpResponse("<h1>Method not Allowed</h1>")
    else:
        edit_id = request.session.get('edit_id')
        if edit_id == None:
            messages.error(request, 'No Id found')
            return HttpResponseRedirect(reverse('manage_ads'))
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
                    return HttpResponseRedirect(reverse('manage_ads'))
                except:
                    messages.error(request, "Failed to Update Your Ads")
                    return HttpResponseRedirect(reverse('edit_ads'))             
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
                        return HttpResponseRedirect(reverse('manage_ads'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads'))
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
                        return HttpResponseRedirect(reverse('manage_ads'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads'))
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
                        return HttpResponseRedirect(reverse('manage_ads'))
                    except:
                        messages.error(request, "Sucesssfully updated Your Ads")
                        return HttpResponseRedirect(reverse('edit_ads'))
            except:
                pass
        return HttpResponseRedirect(reverse('manage_ads'))
    
def notificationCustomer(request):
    allcom = comment.objects.filter(comment_ads__created_by = request.user).order_by('-created_date').exclude(comment_by= request.user)
   
    return render(request, "customer_templates/notification.html", {'all':allcom})

def profile(request):
    loggeduser=  Customer.objects.get(admin = request.user.id)
    
    return render(request, 'customer_templates/profile.html', {'data':loggeduser})
    
        