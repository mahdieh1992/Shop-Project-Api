from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoriesSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from ...models import Category
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CategoryApiView(viewsets.GenericViewSet):
    serializer_class=CategoriesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()

    @method_decorator(cache_page(60*20))#cashing for 20 minutes
    def list(self,request,*args,**kwargs):
        """
         show list along children 
        """
        queryset=self.get_queryset()
        serializer=self.get_serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        # create category with assert if parent equal with 0
        queryset=self.get_queryset()
        data=request.data
        if 'parent' in data:
                parent=data['parent']
                if parent==0:
                    data['parent']=None
        serializer=self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'data':'category success create'},status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
