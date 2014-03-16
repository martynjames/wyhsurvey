from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('yearend',
    url(r'^p1$', views.page1, name='page1'),
    url(r'^p2$', views.page2, name='page2'),
    url(r'^p3$', views.page3, name='page3'),
    url(r'^p4$', views.page4, name='page4'),
    url(r'^p5$', views.page5, name='page5'),
    url(r'^p6$', views.page6, name='page6'),
    url(r'^thanks$', views.thanks, name='thanks'),
)
