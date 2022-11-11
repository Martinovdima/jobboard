from services.views import transcrib
from django.urls import path
app_name = 'services'

urlpatterns = [
    path('', transcrib, name='index'),
]