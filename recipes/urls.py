from django.urls import path
from recipes.views import home

urlpatterns = [
    path('', home), # Chamando a função Home que fica dentro de views
]