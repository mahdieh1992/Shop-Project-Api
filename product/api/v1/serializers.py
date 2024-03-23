from rest_framework import serializers
from ...models import Category

class CategoriesSerializer(serializers.ModelSerializer):
    """
     serializer with get children any parent
    """
    child=serializers.SerializerMethodField() # filed that call method get_child
    CategoryName=serializers.CharField(source='name')# change name to CategoryName
    class Meta:
        model=Category
        fields=('id','CategoryName','child','parent')


    def get_child(self,obj):
        #method for get children any parent
            if obj in Category.objects.all():# if object not in category while category create it's wrong 
                child=obj.get_children()
                return CategoriesSerializer(child,many=True).data


    
    def to_representation(self, instance):
        """
         if the request is get the parent will be popped 
        """
        request=self.context.get('request','GET')
        rep=super().to_representation(instance)
        if request:
            rep.pop("parent")
            return rep
        return rep

 



