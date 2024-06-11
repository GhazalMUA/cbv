from django.urls import path
from . import views
app_name='cbv'
urlpatterns = [
    path(''  ,views.roott , name='roott'),
    path('ghazal/' , views.ghazal.as_view() ) ,
    path('home/' , views.Home.as_view()),
    path('two/' , views.Two.as_view()),
    path('list_kelasha/' , views.KelasList.as_view()),
    path('<int:pk>/' , views.KelasDetail.as_view() , name='kelas_detail'),
    path('form_kelas' , views.FormKelasView.as_view()),
    path('createfoodform/',views.FoodFormView.as_view()),
    path('foodlist/' , views.FoodListView.as_view() , name='food_list'),
    path('delete_food_item/<int:pk>/' , views.DeleteFoodView.as_view() , name='delete_item'),
]