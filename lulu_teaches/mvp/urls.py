from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('lulu_teacher/', include('lulu_teacher.urls')),
    path('admin/', admin.site.urls)
]
