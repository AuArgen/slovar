# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static  # Import the static function

urlpatterns = [
    path('', include('home.urls')),  # Add this line for the main page
    path('admin2024/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

# Add static files serving during development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
