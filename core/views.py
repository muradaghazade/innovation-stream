from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from core.models import News

# Create your views here.
class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firstnews'] = News.objects.order_by('-id').first()
        context['news'] = News.objects.order_by('-id')[1:]
        return context


class NewsDetailView(DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alsoread'] = News.objects.order_by('-id')[1:4]
        self.get_object = self.get_object()
        self.get_object.hit_count +=1
        self.get_object.save()
        print(self.get_object.hit_count)
        return context