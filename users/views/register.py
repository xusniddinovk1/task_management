from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.register import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response({
                'refresh': refresh_token,
                'access': access_token,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
