from django.contrib import admin
from django.urls import path
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_urls.post_list, name='post_list'),
]
    