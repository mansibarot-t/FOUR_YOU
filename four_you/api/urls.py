from django.urls import path
from .views import UserCreateView, UserDetailView, SignupView, LoginView, CartView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user'),
]