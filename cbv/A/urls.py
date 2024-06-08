from django.urls import path
from . import views
app_name='cbv'
urlpatterns = [
    path('ghazal/' , views.ghazal.as_view() ) ,
    path('home/' , views.Home.as_view()),
    path('two/' , views.Two.as_view())
]