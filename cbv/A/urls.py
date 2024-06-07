from django.urls import path
from . import views
app_name='cbv'
urlpatterns = [
    path('' , views.ghazal.as_view() ) ,
]