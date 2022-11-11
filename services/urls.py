from services.views import transcrib, result
from django.urls import path
app_name = 'services'

urlpatterns = [
    path('', transcrib, name='index'),
    path('result/', result, name='result')
]