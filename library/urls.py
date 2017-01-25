"""mylibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^$', views.LoginView.as_view(), name='login'),

    url(r'^library/$', views.HomeView.as_view(), name='home'),
    # url(r'^$', login_required(views.HomeView.as_view()), name='home'),

    url(r'^library/register/$', views.UserFormView.as_view(), name='register'),
    url(r'^library/logout/$', views.LogoutView.as_view(), name='logout'),
    # book/add/
    url(r'^library/book/add/$', views.BookCreate.as_view(), name='book-add'),

    # book/update/2
    url(r'^library/book/update/(?P<pk>[0-9]+)$', views.BookUpdate.as_view(), name='book-update'),

    # book/delete
    url(r'^library/book/delete/(?P<pk>[0-9]+)$', views.BookDelete.as_view(), name='book-delete'),

    # url(r'book/add/(?P<pk>[0-9]+)/$', views.BookCreate.as_view(), name='book-add'),
]

handler404 = 'views.handler404'

handler500 = 'views.handler500'

handler403 = 'views.handler403'
