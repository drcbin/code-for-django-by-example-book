from django.conf.urls import url
from . import views as blog_views


urlpatterns = [
        # url(r'^$', blog_views.post_list, name='post_list'),
        url(r'^$', blog_views.PostListView.as_view(), name='post_list'),
        url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', blog_views.post_detail, name='post_detail'),
        ]