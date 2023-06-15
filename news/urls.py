from django.urls import path

from .views import homePageView, contactView, _404_View, ContactPageView, newsdetailview, newslistview,HomePageView, TechnalogyPageView,SportPageView,ForiegnPageView, LocalPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),

    path('contact_uc/', ContactPageView.as_view(), name='contact_page'),
    path('error_404/', _404_View, name='_404_page'),
    path('news/<slug:news>', newsdetailview, name='detail_page'),
    path('newsall/', newslistview, name='news_lists'),
    path('technalogy/',TechnalogyPageView.as_view(), name='technalogy_news_page'),
    path('sport/',SportPageView.as_view(), name='sport_news_page'),
    path('foriegn/',ForiegnPageView.as_view(), name='foriegn_news_page'),
    path('local/',LocalPageView.as_view(), name='local_news_page'),

]
