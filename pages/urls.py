from django.conf.urls import url
from django.urls import path
from .views import AboutPageView, HomePageView, InfoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('info/', InfoPageView.as_view(), name='info'),
] 
