from django.urls import path
from .views import home, SignInView

urlpatterns = [
    path('', home, name='home'),
    path('login/', SignInView.as_view(), name='login')
]
