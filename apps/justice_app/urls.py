from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^login_reg$', views.login_reg),
    
    url(r'^add_user$', views.add_user), #Registration and Login
    url(r'^login$', views.login),

    url(r'^choose$', views.choose),

    url(r'^health$', views.health),
    url(r'^music$', views.music),
    url(r'^travel$', views.travel),
    url(r'^startup$', views.startup),

    url(r'^add_quote$', views.add_quote),
    url(r'^add_to_list/(?P<id>\d+)$', views.add_to_list),
    url(r'^see_user_posts/(?P<id>\d+)$', views.see_user_posts),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    
    url(r'^logout$', views.logout),
] 