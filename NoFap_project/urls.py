from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #apps
    path('',include('Core_app.urls')),
    #componentes do unicorn
    path("unicorn/", include("django_unicorn.urls")),
    #login
    path('accounts/', include('allauth.urls')),
]
