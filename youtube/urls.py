from django.urls import path

from .views import HomePageView
from .forms import AuthorizeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('auth/', AuthorizeView.as_view(), name='authorize')
]
