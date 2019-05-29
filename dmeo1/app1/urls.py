from django.conf.urls import url
from . import views
app_name='app1'
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.single,name='single'),
    # url(r'^/$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^news/(\d+)/$',views.news,name='news'),
    url(r'^game/$',views.game,name='game'),
    url(r'^fl/(\d+)/$',views.fl,name='fl'),
]