from django.urls import path,include

app_name='product'

urlpatterns = [
    path('api/v1/',include('product.api.v1.urls'),name='api')
]