from .models import News,Category
def latest_news(request):
    latest_news =News.objects.all().order_by('-publish_time').filter(status=News.Status.Published)[:5]
    category_list =Category.objects.all()
    context = {
        'latest_news':latest_news,
        'category_list':category_list

    }
    return context