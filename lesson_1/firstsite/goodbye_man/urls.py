from django.urls import path
from .views import goodbye_man
urlpatterns = [
    path('', goodbye_man, name='goodbye_man')]