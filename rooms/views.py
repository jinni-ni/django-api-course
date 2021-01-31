from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer

# # Create your views here.

@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == 'GET':
        rooms = Room.objects.all()[:5]
        serializer = RoomSerializer(rooms, many=True). data
        return Response(serializer)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serialilzer = RoomSerializer(data=request.data)
        #print(dir(serialilzer))
        # validtation check
        if serialilzer.is_valid():
            room = serialilzer.save(user=request.user)
            room_serializer = RoomSerializer(room).data
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            print(serialilzer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()[:5]
        serializer = RoomSerializer(rooms, many=True).data
        return Response(serializer)

    def post(self,request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serialilzer = RoomSerializer(data=request.data)
        if serialilzer.is_valid():
            room = serialilzer.save(user=request.user)
            room_serializer = RoomSerializer(room).data
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            print(serialilzer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    def get_room(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = RoomSerializer(room).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            # partial=True
            serializer = RoomSerializer(room, data=request.data, partial=True)
            print(serializer.is_valid(), serializer.errors)
            if serializer.is_valid():
                room = serializer.save()
                return Response(RoomSerializer(room).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        room = self.get_room(pk)

        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# class SeeRoomView(RetrieveAPIView):
#     queryset = Room.objects.all()
#     serializer_class =ReadRoomSerializer

# @api_view(["GET", "DELETE"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms, many=True)
#     return Response(data=serialized_rooms.data)


# class ListRoomView(APIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
#
# class ListRoomView(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

