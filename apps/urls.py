
from django.urls import path

from .views import Home_pageView

urlpatterns = [
    path('', Home_pageView.as_view(), name='home_page'),
]
