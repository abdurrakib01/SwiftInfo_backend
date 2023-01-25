from django.urls import path
from .views import UserRegistraionView, UserLoginView, SendPasswordResetView, UserPasswordResetView, UserProfileView
from .views import UserInformationView, PostUserInformationView
urlpatterns = [
    path('register/', UserRegistraionView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name="user"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userinfo/', PostUserInformationView.as_view(), name='userinfo'),
    path('userinfo/<int:pk>/', UserInformationView.as_view(), name='info'),
    path('send-password-reset/', SendPasswordResetView.as_view(), name="send-password-reset"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetview'),
]