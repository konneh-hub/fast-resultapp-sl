"""
Main URL Configuration for fastresult_backend.
Routes all app-specific URLs through this central configuration.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/universities/', include('universities.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/students/', include('students.urls')),
    path('api/lecturers/', include('lecturers.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/results/', include('results.urls')),
    path('api/approvals/', include('approvals.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/notifications/', include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
