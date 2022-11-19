from services.views import transcrib, create, transcribation_result
from django.urls import path

app_name = 'services'

urlpatterns = [
    path('', transcrib, name='index'),
    path('create/', create, name='create'),
    path('transcribation_result/', transcribation_result, name='transcribation_result')
]
