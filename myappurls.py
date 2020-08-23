from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),           # r--> regular expression,  ^$ --> root url(localhost)
    url(r'^test',views.test,name='test'),

]