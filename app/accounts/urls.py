from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout')
]