from django import forms
from .models import ImagesAd
from django.core.exceptions import ValidationError

selling_in = (
    ('Fixed', 'Fixed Price'),
    ('Bargainable', 'Bragainable')
)
face_toward = (
    ('East', 'East'),
    ('West', 'West'),
    ('North', 'North'),
    ('South', 'South')
)
YesNo = (
    ('Yes', 'YES'),
    ('No', 'No')   
)

district = (
        ('Kathmandu','Kathmandu'),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur'),
        ('Makwanpur','Makwanpur'),
        ('Chitwan','Chitwan'),
        ('Dhading','Dhading'),
        ('Dhankuta','Dhankuta'),
        ('Gorkha','Gorkha'),
        ('Jhapa','Jhapa'),
        ('Kaski','Kaski'),
        ('Kavrepalanchok','Kavrepalanchok'),
        ('Sindhupalchok','Sindhupalchok'),
        ('Solukhumbu','Solukhumbu'),
        ('Surkhet','Surkhet'),
        ('Taplejung','Taplejung'),
        ('Other','Other')
    )
class CustomerForm(forms.Form):
    email = forms.EmailField(label= "Email", max_length=50, widget = forms.EmailInput(attrs={'class':"form-control"}))
    first_name = forms.CharField(label= "First Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    last_name  = forms.CharField(label= "Last Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    # username = forms.CharField(label= "Username", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    address = forms.CharField(label= "Address", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    number = forms.CharField(label = "Number", max_length=10, widget = forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label= "Password", max_length=50, widget = forms.PasswordInput(attrs={'class':"form-control"}))
    
    
class AddHouse(forms.Form):
    title = forms.CharField(label= 'Title', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Example: 3 Floor House for sale'}))
    district = forms.ChoiceField(label= 'District', choices = district, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Example: Kathmandu'}))
    woda = forms.IntegerField(label = 'Ward number', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder': '5'}))
    location = forms.CharField(label= 'Street Address', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Baneshowr, Thapa Gau'}))
    price = forms.CharField(label= 'Price', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price- 2000000'}))
    price_in_words = forms.CharField(label= 'Price in Words', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price in Word- '}))
    selling_in = forms.ChoiceField(label= 'Selling Pirce', choices = selling_in, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Selling In-Bragainable'}))
    landsize = forms.CharField(label= 'Land Area Size', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Land Size- 10 Anna'}))
    roadsize = forms.CharField(label= 'Road Size', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Road Size- 10 Feet'}))
    floor = forms.IntegerField(label = 'No. of Floor', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Floor- 3'}))
    bedroom = forms.IntegerField(label = 'No. of bedroom', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Bedroom- 10'}) )
    bathroom = forms.IntegerField(label = 'No. of bathroom', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Bathroom-5'}) )
    kitchen = forms.IntegerField(label = 'No. of kitchen', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Kitchen-3'}) )
    face_towards = forms.ChoiceField(label= 'Face Towards',  choices = face_toward, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    garden = forms.ChoiceField(label= 'Garden', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    garage = forms.ChoiceField(label= 'Garage', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    undergroundtank = forms.ChoiceField(label= 'Underground Tank', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    description = forms.CharField(label= 'Property Description', widget = forms.Textarea(attrs={'class':"form-control", 'placeholder':'Describe your property!'}))
    house_pic = forms.FileField(label= "Thumbnail for House Picture", max_length=50, widget = forms.FileInput(attrs={'class':"form-control"}), required = False)

    def clean_landsize(self):
        data = self.cleaned_data['landsize']
        
        try: 
            da = int(data)
        except:
            return data
        raise ValidationError("Do not only include number! Input like {} Anna".format(da))
        
    def clean_woda(self):
        data = self.cleaned_data['woda']
        if type(data) == 'str':
            raise ValidationError("Please Write Your Woda Number Correctly")
        return data
    def clean_price(self):
        data = self.cleaned_data['price']
        aa = str(data)
        if len(aa) < 3:
            raise ValidationError('Please write full Amout')
        return data
    def clean_roadsize(self):
        data = self.cleaned_data['roadsize']
        try: 
            da = int(data)
        except:
            return data
        raise ValidationError("Do not only include number! Input like {} Foot or Len".format(da))

class LandForm(forms.Form):
    title = forms.CharField(label= 'Title', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Example: 3 Floor House for sale'}))
    district = forms.ChoiceField(label= 'District', choices = district, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Example: Kathmandu'}))
    woda = forms.IntegerField(label = 'Ward number', widget = forms.TextInput(attrs={'class':"form-control ", 'placeholder': '5'}))
    location = forms.CharField(label= 'Street Address', widget = forms.TextInput(attrs={'class':"form-control ", 'placeholder':'Baneshowr, Thapa Gau'}))
    price = forms.CharField(label= 'Price', widget = forms.TextInput(attrs={'class':"form-control ", 'placeholder':'Price- 2000000'}))
    price_in_words = forms.CharField(label= 'Price in Words', widget = forms.TextInput(attrs={'class':"form-control ", 'placeholder':'Price in Word- '}))
    selling_in = forms.ChoiceField(label= 'Selling Pirce', choices = selling_in, widget = forms.Select(attrs={'class':"form-control ", 'placeholder':'Selling In-Bragainable'}))
    landsize = forms.CharField(label= 'Land Area Size', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Land Size- 10 Anna'}))
    roadsize = forms.CharField(label= 'Road Size', widget = forms.TextInput(attrs={'class':"form-control ", 'placeholder':'Road Size- 10 Feet'}))
    electricity = forms.ChoiceField(label= 'Electricity Line', choices = YesNo, widget = forms.Select(attrs={'class':"form-control col-12", 'placeholder':'Electricity Line'}))
    plotting = forms.ChoiceField(label= 'Plotting', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Plotting'}))
    description = forms.CharField(label= 'Property Description', widget = forms.Textarea(attrs={'class':"form-control ", 'placeholder':'Describe your property!'}))
    land_pic = forms.FileField(label= "Land Picture", max_length=50, widget = forms.FileInput(attrs={'class':"form-control "}), required = False)

    def clean_landsize(self):
        data = self.cleaned_data['landsize']
        try: 
            da = int(data)
        except:
            return data
        raise ValidationError("Do not only include number! Input like {} Anna".format(da))
        return data
    def clean_woda(self):
        data = self.cleaned_data['woda']
        if type(data) == 'str':
            raise ValidationError("Please Write Your Woda Number Correctly")
        return data
    def clean_price(self):
        data = self.cleaned_data['price']
        aa = str(data)
        if len(aa) < 3:
            raise ValidationError('Please write full Amout')
        return data
    def clean_roadsize(self):
        data = self.cleaned_data['roadsize']
        try: 
            da = int(data)
        except:
            return data
        raise ValidationError("Do not only include number! Input like {} Foot or Len".format(da))

class RentForm(forms.Form):
    
    title = forms.CharField(label= 'Title', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Example: 3 Floor House for sale'}))
    district = forms.ChoiceField(label= 'District', choices = district, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Example: Kathmandu'}))
    woda = forms.IntegerField(label = 'Ward number', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder': '5'}))
    location = forms.CharField(label= 'Street Address', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Baneshowr, Thapa Gau'}))
    price = forms.CharField(label= 'Price', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price- 2000000'}))
    price_in_words = forms.CharField(label= 'Price in Words', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price in Word- '}))
    selling_in = forms.ChoiceField(label= 'Selling Pirce', choices = selling_in, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Selling In-Bragainable'}))
    rentroom = forms.IntegerField(label = 'No. of Room', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'No. of Room'}) )
    bathroom = forms.IntegerField(label = 'No. of bathroom', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Bathroom-5'}) )
    internet = forms.ChoiceField(label= 'Internet Connection', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    garage = forms.ChoiceField(label= 'Garage', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    tvchannel = forms.ChoiceField(label= 'TV channel', choices = YesNo, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Location'}))
    description = forms.CharField(label= 'Property Description', widget = forms.Textarea(attrs={'class':"form-control", 'placeholder':'Describe your property!'}))
    rent_pic = forms.FileField(label= "Room Picture", max_length=50, widget = forms.FileInput(attrs={'class':"form-control"}), required = False)

    
    def clean_woda(self):
        data = self.cleaned_data['woda']
        if type(data) == 'str':
            raise ValidationError("Please Write Your Woda Number Correctly")
        return data
    def clean_price(self):
        data = self.cleaned_data['price']
        aa = str(data)
        if len(aa) < 3:
            raise ValidationError('Please write full Amout')
        return data
    
class BusinessForm(forms.Form):
    title = forms.CharField(label= 'Title', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Example: 3 Floor House for sale'}))
    district = forms.ChoiceField(label= 'District', choices = district, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Example: Kathmandu'}))
    woda = forms.IntegerField(label = 'Ward number', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder': '5'}))
    location = forms.CharField(label= 'Street Address', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Baneshowr, Thapa Gau'}))
    price = forms.CharField(label= 'Price', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price- 2000000'}))
    price_in_words = forms.CharField(label= 'Price in Words', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Price in Word- '}))
    selling_in = forms.ChoiceField(label= 'Selling Pirce', choices = selling_in, widget = forms.Select(attrs={'class':"form-control", 'placeholder':'Selling In-Bragainable'}))
    business = forms.CharField(label= 'Business Type', widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':'Business Type - Hotel, Store '}))
    description = forms.CharField(label= 'Property Description', widget = forms.Textarea(attrs={'class':"form-control", 'placeholder':'Describe your property!'}))
    business_pic = forms.FileField(label= "Room Picture", max_length=50, widget = forms.FileInput(attrs={'class':"form-control"}), required = False)

    def clean_woda(self):
        data = self.cleaned_data['woda']
        if type(data) == 'str':
            raise ValidationError("Please Write Your Woda Number Correctly")
        return data
    def clean_price(self):
        data = self.cleaned_data['price']
        aa = str(data)
        if len(aa) < 3:
            raise ValidationError('Please write full Amout')
        return data

class EditUserProfile(forms.Form):
    email = forms.EmailField(label= "Email", max_length=50, widget = forms.EmailInput(attrs={'class':"form-control"}))
    first_name = forms.CharField(label= "First Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    last_name  = forms.CharField(label= "Last Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    address = forms.CharField(label= "Address", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    number = forms.CharField(label = "Number", max_length=10, widget = forms.TextInput(attrs={'class':"form-control"}))
    profile_pic = forms.FileField(label= "Profile Picture", widget = forms.FileInput(attrs={'class':"form-control"}) )
    

class EditAdminProfile(forms.Form):
    email = forms.EmailField(label= "Email", max_length=50, widget = forms.EmailInput(attrs={'class':"form-control"}))
    first_name = forms.CharField(label= "First Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    last_name  = forms.CharField(label= "Last Name", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
    # username = forms.CharField(label= "Username", max_length=50, widget = forms.TextInput(attrs={'class':"form-control"}))
   
   
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='', widget = forms.FileInput(attrs={'class':"form-control"}))    
    class Meta:
        model = ImagesAd
        fields = ('image', )