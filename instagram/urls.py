"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

"""we import this for jwt token create, refresh, verify"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

"""we create default url which call user api"""
router = DefaultRouter()
router.register("user",views.Userapi, basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    #"when we call curd url it will give as student url by which we can use our api"
    path("curd/", include(router.urls)),
    path("gettoken/", TokenObtainPairView.as_view(), name="token"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verifytoken/", TokenVerifyView.as_view(), name="token_verify"),
]