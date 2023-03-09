from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from core.models import News, Category, Subscriber
from django.db.models import Q
from core.forms import SubscriberForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

from django.http import HttpResponse
# from core.tasks import send_mail_func


class MainPageView(FormMixin, ListView):
    template_name = 'index.html'
    model = News
    context_object_name = 'news'
    paginate_by = 6
    form_class = SubscriberForm
    success_url = reverse_lazy('core:main')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firstnews'] = News.objects.filter(main=True).first()
        context['categories'] = Category.objects.all()
        # context['form'] = SubscriberForm()
        return context

    def get_queryset(self):
        queryset = News.objects.filter(main=False).order_by('-id')
        return queryset
    
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if form.is_valid():
                return self.form_valid(form)
            else:
                raise ValidationError("Email already exists")
                
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NewsDetailView(FormMixin, DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = "news"
    form_class = SubscriberForm
    success_url = reverse_lazy('core:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alsoread'] = News.objects.order_by('-id')[1:4]
        context['categories'] = Category.objects.all()
        self.get_object = self.get_object()
        self.get_object.hit_count +=1
        self.get_object.save()
        return context
    
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if form.is_valid():
                return self.form_valid(form)
            else:
                raise ValidationError("Email already exists")
                
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchNewsView(FormMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = 'search.html'
    form_class = SubscriberForm
    success_url = reverse_lazy('core:main')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        queryset = News.objects.order_by('-id')

        if title:
            queryset = queryset.filter(Q(title__icontains=title) | Q(tags__title__icontains=title))
        if category:
            queryset = queryset.filter(category__title=category)
        return queryset
    
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if form.is_valid():
                return self.form_valid(form)
            else:
                raise ValidationError("Email already exists")
                
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

# class SubscriberView(CreateView):
#     model = Subscriber
#     form_class = SubscriberForm
#     uccess_url = reverse_lazy('main')
# def send_mail_to_all(request): 
#     send_mail_func.delay()  
#     return HttpResponse("Sent Email Successfully...Check your mail please")