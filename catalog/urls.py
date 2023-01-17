from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts  # (*)

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),  # http://127.0.0.1:8000
    path('contacts/', contacts),  # http://127.0.0.1:8000/contacts/
]
