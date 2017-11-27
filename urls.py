from django.conf.urls import url
from django.contrib import admin
from library import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^booksearch/', views.booksearch, name='booksearch'),
    url(r'^finesrefresh/', views.finesrefresh, name='finesrefresh'),
    url(r'^finespay/', views.finespay, name='finespay'),
    url(r'^', views.main, name='main'),
    url(r'^main/', views.main, name='main'),
]

