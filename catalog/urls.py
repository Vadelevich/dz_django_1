from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home,contacts # (*)

app_name = CatalogConfig.name

urlpatterns = [
    path('',home), # http://127.0.0.1:8000/home
    path('contacts/',contacts),  #http://127.0.0.1:8000/home/contacts/
]