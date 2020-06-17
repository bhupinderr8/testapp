from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from auth.views import 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('home/', include('myapp.urls')),
]
