

from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView,ListView

from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import News,Category


def newslistview(request):
    news_list = News.objects.all().order_by('-publish_time').filter(status=News.Status.Published)
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)


def newsdetailview(request, news):
    news_list = get_object_or_404(News, slug=news,status=News.Status.Published)
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    news_list =News.objects.all().order_by('-publish_time').filter(status=News.Status.Published)[:5]
    categories=Category.objects.all()    
    local_list =News.objects.all().filter(status=News.Status.Published).filter(category__name="Mahalliy").order_by('-publish_time')[:6]
    context = {
            'news_list':news_list,
            'categories':categories,
            'local_list':local_list,
            'local_one':local_one
    }    
    return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model =News
    template_name = 'news/home.html'
    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time').filter(status=News.Status.Published)[:5]        
        context['local_list'] =News.objects.all().filter(status=News.Status.Published).filter(category__name="Mahalliy").order_by('-publish_time')[:6]
        context['sport_list'] =News.objects.all().filter(status=News.Status.Published).filter(category__name="Sport").order_by('-publish_time')[:6]
        context['xorij_list'] =News.objects.all().filter(status=News.Status.Published).filter(category__name="Jahon").order_by('-publish_time')[:6]
        context['texnologiya_list'] =News.objects.all().filter(status=News.Status.Published).filter(category__name="Texnologiya").order_by('-publish_time')[:6]
        

        return context


class LocalPageView(ListView):
    model = News
    template_name ="news/local.html"
    context_object_name ='local_list'
    
    def get_queryset(self):
        news =self.model.objects.all().filter(status =News.Status.Published).filter( category__name="Mahalliy")
        return news
    
class TechnalogyPageView(ListView):
    model = News
    template_name ="news/technology.html"
    context_object_name ='texnologiya_list'
    
    def get_queryset(self):
        news =self.model.objects.all().filter(status =News.Status.Published).filter( category__name="Texnologiya")
        return news


class SportPageView(ListView):
    model = News
    template_name ="news/sport.html"
    context_object_name ='sport_list'
    
    def get_queryset(self):
        news =self.model.objects.all().filter(category__name="Sport")
        return news


class ForiegnPageView(ListView):
    model = News
    template_name ="news/foriegn.html"
    context_object_name ='xorij_yangiliklari'
    
    def get_queryset(self):
        news =self.model.objects.all().filter(status =News.Status.Published, category__name="Jahon").order_by('-publish_time')
        return news



def contactView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> Biz bilan bog'langaniz uchun raxmat. </h2>")
    context = {
        'form': form

    }
    return render(request, 'news/contact.html', context)


def _404_View(request):
    context = {

    }
    return render(request, 'news/404.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaniz uchun raxmat.</h2>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


