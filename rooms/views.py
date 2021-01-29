from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer

# # Create your views here.


@api_view(["GET", "DELETE"])
def list_rooms(request):
    rooms = Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)


# class ListRoomView(APIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)

class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
