from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
path("",views.index,name='home'),
path("market",views.market,name='market'),
path("news",views.news,name='News'),
path('search',views.search,name="Search"),
path('search2',views.search2,name="Search2")
]
