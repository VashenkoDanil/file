from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from file.views import MultipleFilesView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MultipleFilesView.as_view(), name='multiple_files'),
]
