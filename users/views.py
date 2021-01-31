from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ReadUserSerializer, WriteUserSerializer
from .models import User
# Create your views here.
class MeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(ReadUserSerializer(request.user).data)

    def put(self, request):
        serailizer = WriteUserSerializer(request.user, data=request.data, partial=True)
        if serailizer.is_valid():
            serailizer.save()
            return Response()
        else:
            return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
