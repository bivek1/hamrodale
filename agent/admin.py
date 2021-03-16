from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,  Customer, AdminOwner, advertise, house, land, rent,requestBuy, ImagesAd ,comment, business
# Register your models here.
class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser, UserModel)
admin.site.register(AdminOwner)
admin.site.register(Customer)
admin.site.register(advertise)
admin.site.register(house)
admin.site.register(land)
admin.site.register(rent)
admin.site.register(business)
admin.site.register(comment)
admin.site.register(requestBuy)
admin.site.register(ImagesAd)

