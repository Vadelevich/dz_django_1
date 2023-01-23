from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product, Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.urls import reverse_lazy, reverse


def contacts(request):
    return render(request, 'catalog/contacts.html')


class HomeListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ArticleListView(ListView):
    model = Article

    def get_queryset(
            self):  # Переопределим родит., выводить в список статей только те, который имеют положительный признак публикации
        queryset = super().get_queryset()
        queryset = queryset.filter(publicate=Article.STATUSE_ACTIVE)

        return queryset


class ArticleCreateView(CreateView):
    model = Article
    # fields = '__all__'
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('catalog:blog')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('catalog:blog')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:blog')
    context_object_name = 'news_item'


class ArticleDetailView(DetailView):
    model = Article

    def get(self, request, pk):  # Переопределяем родительский метод для подсчета просмотров
        block_item = get_object_or_404(Article, pk=pk)
        block_item.count += 1
        block_item.save()
        return super().get(self, request, pk)


def change_status(request, pk):
    # block_item = Article.objects.get(pk=pk)
    # block_item = Article.objects.filter(pk=pk).first()
    # if block_item:
    #     ...
    block_item = get_object_or_404(Article, pk=pk)
    if block_item.publicate == Article.STATUSE_ACTIVE:
        block_item.publicate = Article.STATUSE_INACTIVE
    else:
        block_item.publicate = Article.STATUSE_ACTIVE
    block_item.save()

    return redirect(reverse('catalog:blog'))
