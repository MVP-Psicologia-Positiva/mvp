from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('app/', include('frontend.urls')),
    path('api/', include('lulu_teacher.urls')),
    path('accounts/',include('allauth.urls'))
]
