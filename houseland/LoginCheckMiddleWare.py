from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "adminViews":
                    pass
                elif modulename == 'views' or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_page"))
            elif user.user_type == "2":
                if modulename == "customer_Views":
                    pass
                elif modulename == 'views' or modulename == "django.views.static" or  modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("customer_page"))
        else:
            if modulename == "customer_Views":
                pass
            elif modulename == 'views' or modulename == "django.views.static" or  modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("customer_page"))


            
    