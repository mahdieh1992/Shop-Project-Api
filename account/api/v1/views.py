from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class LoginUserView(GenericAPIView):
    serializer_class=UserLoginSerializer

    def post(self,request):
        """
            login user with receive token
        """
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.validated_data.get('user')
            if user.is_staff:
                token,created=Token.objects.get_or_create(user=user)
                return Response({'user':
                                 {'email':user.email,
                                  'token':token.key
                                    }},status=status.HTTP_200_OK)
            return Response({'detail':'User is blocked'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

