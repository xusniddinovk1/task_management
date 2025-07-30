from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.login import LoginSerializer
from drf_yasg.utils import swagger_auto_schema


class LoginVIew(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response({
                'refresh': str(refresh_token),
                'access': str(access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
