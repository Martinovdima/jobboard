from services.views import transcrib, create
from django.urls import path

app_name = 'services'

urlpatterns = [
    path('', transcrib, name='index'),
    path('create/', create, name='create')
]
