from django.conf.urls import url
from testapp import views

urlpatterns = [

url(r'^$',views.index,name='index'),
url(r'^Course2/$',views.course,name='course2'),
url(r'^Course2/Chapter2/$',views.chapter2,name='chapter2'),
url(r'^Course/Chapter2/simulation-load-balancing/$',views.simulation1,name='simulation-load-balancing'),
url(r'^Course/Chapter2/simulation-distributed-caching/$',views.simulation2,name='simulation-distributed-caching'),
url(r'^Course2/Chapter2/Content$',views.content_fetch,name='content'),

]