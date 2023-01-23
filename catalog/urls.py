from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, ArticleListView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView, ArticleDetailView, change_status

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),  # http://127.0.0.1:8000
    path('contacts/', contacts, name='contacts'),  # http://127.0.0.1:8000/contacts/
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('blog-list/', ArticleListView.as_view(), name='blog'),
    path('blog-create/', ArticleCreateView.as_view(), name='create'),
    path('blog-update/<int:pk>/',ArticleUpdateView.as_view(),name='update'),
    path('blog-delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('blog-detail/<int:pk>/', ArticleDetailView.as_view(), name='detail_block'),
    path('blog-status/<int:pk>/', change_status, name='status'),
]
