
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),

]
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
