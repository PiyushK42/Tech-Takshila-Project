from django.conf.urls import url
from testapp import views

urlpatterns = [

url(r'^$',views.index,name='index'),
url(r'^Course2/$',views.course,name='course2'),
url(r'^distributed_system/consistent-hashing/$',views.chapter2,name='chapter2'),
url(r'^distributed_system/$',views.subject_page,name='ds'),
url(r'^distributed_system/consistent-hashing/simulation-load-balancing/$',views.simulation1,name='simulation-load-balancing'),
url(r'^distributed_system/consistent-hashing/simulation-distributed-caching/$',views.simulation2,name='simulation-distributed-caching'),
url(r'^distributed_system/CAP-theorem/$',views.chapter1,name='content'),

]