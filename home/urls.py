from django.urls import path
from home import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('speak-translate/', views.speak_translate, name='speak-translate'),
    # path('translate/', views.TextTranslateView.as_view(), name='translate'),
    path('translate/', views.translate, name='translate'),
]