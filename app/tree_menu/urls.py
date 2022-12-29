from django.contrib import admin
from django.urls import path

from menu.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', index.as_view(), name='index'),
    path('', index.as_view())
]
