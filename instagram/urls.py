from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from user import views
from post import views
# from follow import views

"""we import this for jwt token create, refresh, verify"""
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# """we create default url which call user api"""
# router = DefaultRouter()
# router.register("user",views.Userapi, basename="user")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #"when we call curd url it will give as student url by which we can use our api"
#     path("curd/", include(router.urls)),
#     path("gettoken/", TokenObtainPairView.as_view(), name="token"),
#     path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
#     path("verifytoken/", TokenVerifyView.as_view(), name="token_verify"),
# ]  

# router.register('student', views., basename='student_')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('postapi/', views.PostListCreate.as_view()),
    path('postapi/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view()),
]
# urlpatterns += router.urls