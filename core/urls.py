from django.urls import path
from core.views import MainPageView, NewsDetailView, SearchNewsView

app_name = 'core'


urlpatterns = [
    path('',MainPageView.as_view(),name ='main'),
    path('search/',SearchNewsView.as_view(),name ='search'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news'),
    # path('sendmail/', send_mail_to_all, name="sendmail"),
]