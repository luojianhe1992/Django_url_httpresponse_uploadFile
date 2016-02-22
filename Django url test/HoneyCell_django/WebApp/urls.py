__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # empty url
    url(r'^$', 'WebApp.views.index', name='index'),

    # new argument 'template_name'
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'WebApp/login.html'}, name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'WebApp.views.my_logout', name='logout'),

    # registration is normal route
    url(r'^registration/$', 'WebApp.views.registration', name='registration'),

    # after login, show the message page to the user
    url(r'^message/$', 'WebApp.views.message', name='message'),

    # go to upload page
    url(r'^upload/$', 'WebApp.views.upload', name='upload'),

    # go to preprocess page
    url(r'preprocess/$', 'WebApp.views.preprocess', name='preprocess'),

    # go to visualization page
    url(r'visualization/$', 'WebApp.views.visualization', name='visualization'),

    # go to honeycell page
    url(r'honeycell/$', 'WebApp.views.honeycell', name='honeycell'),

    # go to honeycomb page
    url(r'honeycomb/$', 'WebApp.views.honeycomb', name='honeycomb'),

    # go to analytics page
    url(r'analytics/$', 'WebApp.views.analytics', name='analytics'),

    url(r'url_test/$', 'WebApp.views.url_test', name='url_test'),

    url(r'url_test_2/$', 'WebApp.views.url_test_2', name='url_test_2'),

    url(r'url_test_3/$', 'WebApp.views.url_test_3', name='url_test_3'),

    url(r'upload_test/$', 'WebApp.views.upload_test', name='upload_test'),

    url(r'show_files/$', 'WebApp.views.show_files', name='show_files'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)