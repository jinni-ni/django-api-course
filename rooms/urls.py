from django.urls import path
from . import views
from . import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


app_name = "rooms"
router.register("", viewsets.RoomViewSet, basename="room" )

urlpatterns = router.urls

# urlpatterns = [
    # path("list/", views.ListRoomView.as_view()),
    # path("<int:pk>/", views.SeeRoomView.as_view()),
# ]
