from django.urls import path
from Login import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
app_name="Login"

urlpatterns=[
path('signup/',views.sign_up,name='signup'),
path('login/',views.login_page,name='login'),
path('logout/',views.logout_user,name='logout'),
path('profile/',views.profile,name='profile'),
path('change-profile/',views.user_change,name='change-profile'),
path('pic_add/',views.add_pro_pic,name='pic_add'),
]
