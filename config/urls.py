from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms/", include("core.urls")),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/users/", include("users.urls")),
    # path("api/v2/rooms/", include("rooms_v2.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

