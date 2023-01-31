from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from user import views
# from post import views
# from story import views
# from comment import views
# from like import views
# from share import views 
# from story.views import StoryViewSet
# from reels import views
# from reels.views import ReelViewSet
# from follow import views
from direct_message import views


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

# router.register('student', views.postapi, basename='student_')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('postapi/', views.PostAPI.as_view()),
#     path('postapi/<int:pk>/', views.PostAPI.as_view()),
# ]


# router = DefaultRouter()
# router.register(r'story', StoryViewSet, basename= 'story')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('storyapi/', views.StoryAPI.as_view()),
#     path('storyapi/<int:pk>/', views.StoryAPI.as_view()),
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('reelsapi/', views.ReelsAPI.as_view()),
#     path('reelsapi/<int:pk>/', views.ReelsAPI.as_view()),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('commentapi/', views.CommentAPI.as_view()),
#     # path('commentapi/<int:pk>/', views.CommentAPI.as_view()),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('likeapi/', views.LikeAPI.as_view()),
#     path('likeapi/<int:pk>/', views.LikeAPI.as_view()),
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('shareapi/', views.ShareAPI.as_view()),
#     path('shareapi/<int:pk>/', views.ShareAPI.as_view()),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('followapi/', views.FollowAPI.as_view()),
#     path('followapi/<int:pk>/', views.FollowAPI.as_view()),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directmessageapi/', views.DirectMessageAPI.as_view()),
    path('directmessageapi/<int:pk>/', views.DirectMessageAPI.as_view()),
]