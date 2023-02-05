from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Article, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.urls import reverse_lazy, reverse


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductListView(LoginRequiredMixin,ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    
    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)   # Подготовиться обьект с данными из формы
            self.object.user_create = self.request.user  # В поле user_create запишится пользователь который делает запрос
            self.object.save()
        return super().form_valid(form)
            

class ProductUpdateView(UserPassesTestMixin,UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    def get_queryset(self):
        return Product.objects.filter(user_create=self.request.user)

    def test_func(self):
        product = self.get_object()
        return product.user_create == self.request.user or self.request.user.has_perms(perm_list=['change_title_product','set_category_product','set_status_product',])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

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

@login_required
def change_status(request, pk):
    # block_item = Article.objects.get(pk=pk)
    # block_item = Article.objects.filter(pk=pk).first()
    # if block_item:
    #     ...
    block_item = get_object_or_404(Article, pk=pk)
    if block_item.published == Article.STATUSE_ACTIVE:
        block_item.published = Article.STATUSE_INACTIVE
    else:
        block_item.published = Article.STATUSE_ACTIVE
    block_item.save()

    send_mail(
        subject='hgvjgvhg',
        message='jhvjvv',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['vadelevich2013@yandex.ru']
    )
    return redirect(reverse('catalog:blog'))


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_with_version.html'

    def get_success_url(self):
        return reverse('catalog:detail',args=[self.object.pk])
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model,Version,form=VersionForm,extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data ['formset'] = formset
        return context_data
    
    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print(self.request.method)
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

