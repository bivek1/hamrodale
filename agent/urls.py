from django.urls import path
from .import views, adminViews, customer_Views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('register', views.register, name = 'register'),
    path('login', views.loginpage, name = "login"),
    path('dologin', views.dologin, name="dologin"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'), 
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout', views.logout_user, name = "logout"),
    path('houseforsell', views.house_page, name = "house_page"),
    path('landforsell', views.land_page, name = "land_page"),
    path('rentforsell', views.rent_page, name = "rent_page"),
    path('businessforsell', views.business_page, name = "business_page"),
    path('details_page/ads_id=<str:ads_id>', views.details, name="details_page"),
    path('delete_cmt/cmt_id=<str:cmt_id>', views.delete_cmt, name = 'delete_cmt'),
    path('request/<str:ads_id>', views.requestads, name= 'request'),
    path('premiumlist', views.premium_list, name = "premium_list"),
    path('featurelist', views.feature_list, name = "feature_list"),
    path('search', views.search, name = "search"),
    path('searchads', views.searchads, name = 'searchads'),

    # Reset the Password
    
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # Admin page path
    path('admin_page', adminViews.admin_page, name = "admin_page"),
    path('total_ads', adminViews.total_ads, name = "total_ads"),
    path('total_member', adminViews.total_member, name = 'total_member'),
    path('update_profile_admin', adminViews.update_profile, name = "update_profile_admin" ),
    path('update_profile_save_admin', adminViews.update_profile_save, name = 'update_profile_save_admin'),
    path('add_house_admin', adminViews.add_house, name = 'add_house_admin'),
    path('add_house_save_admin', adminViews.add_house_save, name = 'add_house_save_admin'),
    path('add_land_admin', adminViews.add_land, name = 'add_land_admin'),
    path('add_land_save_admin', adminViews.add_land_save, name = 'add_land_save_admin'),
    path('add_rent_admin', adminViews.add_rent, name = 'add_rent_admin'),
    path('add_rent_save_admin', adminViews.add_rent_save, name = 'add_rent_save_admin'),
    path('add_business_admin', adminViews.add_business, name = 'add_business_admin'),
    path('add_business_save_admin', adminViews.add_business_save, name = 'add_business_save_admin'),
    path('manage_ads_admin', adminViews.manage_ads, name = 'manage_ads_admin'),
    path('delete_ads_admin/<str:id>', adminViews.delete_ads, name = 'delete_ads_admin'),
    path('edit_ads_admin/<str:edit_id>', adminViews.edit_ads, name= 'edit_ads_admin'),
    path('edit_ads_save_admin', adminViews.edit_ads_save, name = 'edit_ads_save_admin'),
    path('requested_ads', adminViews.requested, name="requestads"),
    path('premium_ads', adminViews.premium_ads, name = 'premium'),
    path('features_ads', adminViews.features_ads, name = 'features'),
    path('remove_premium/<str:ads_id>', adminViews.remove_premium, name = 'remove_premium'),
    path('remove_features/<str:ads_id>', adminViews.remove_feature, name = 'remove_feature'),
    path('add_dealed/<str:ad_id>', adminViews.add_dealed, name = "add_dealed"),
    path('notification_admin', adminViews.notification, name = 'notification_admin'),
    
    # Customer page Path
    path('customer_page', customer_Views.customer_page, name="customer_page"),
    path('update_profile', customer_Views.update_profile, name = "update_profile" ),
    path('update_profile_save', customer_Views.update_profile_save, name = 'update_profile_save'),
    path('add_house', customer_Views.add_house, name = 'add_house'),
    path('add_house_save', customer_Views.add_house_save, name = 'add_house_save'),
    path('add_land', customer_Views.add_land, name = 'add_land'),
    path('add_land_save', customer_Views.add_land_save, name = 'add_land_save'),
    path('add_rent', customer_Views.add_rent, name = 'add_rent'),
    path('add_rent_save', customer_Views.add_rent_save, name = 'add_rent_save'),
    path('add_business', customer_Views.add_business, name = 'add_business'),
    path('add_business_save', customer_Views.add_business_save, name = 'add_business_save'),
    path('manage_ads', customer_Views.manage_ads, name = 'manage_ads'),
    path('delete_ads/<str:id>', customer_Views.delete_ads, name = 'delete_ads'),
    path('edit_ads/<str:edit_id>', customer_Views.edit_ads, name= 'edit_ads'),
    path('edit_ads_save', customer_Views.edit_ads_save, name = 'edit_ads_save'),
    path('notification_customer', customer_Views.notificationCustomer, name = 'notification_customer'),
    path('userprofile', customer_Views.profile, name = 'profile'),
]
