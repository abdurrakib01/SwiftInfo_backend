from django.urls import path
from .views import UserRegistraionView, UserLoginView, SendPasswordResetView, UserPasswordResetView, UserProfileView
urlpatterns = [
    path('register/', UserRegistraionView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name="user"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('send-password-reset/', SendPasswordResetView.as_view(), name="send-password-reset"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetview'),
]