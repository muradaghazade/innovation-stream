from django.urls import path
from core.views import MainPageView, NewsDetailView

app_name = 'core'


urlpatterns = [
    path('',MainPageView.as_view(),name ='main'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news'),
]