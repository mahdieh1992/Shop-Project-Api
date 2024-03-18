import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from faker import Faker
from django.urls import reverse


fake=Faker()
user=get_user_model()

@pytest.fixture
def api_client():
    client=APIClient()
    return client


first_name=fake.first_name()
data={
    'email':f'{first_name}@gmail.com',
    'password':'1234!@#$'
}
print(f'{first_name}@gmail.com')


@pytest.fixture
def create_user():
    new_user=user.objects.create_user(email=data['email'],password=data['password'],is_active=True,is_staff=True)
    return new_user


@pytest.mark.django_db
class Test_User:
    """
     testing for login user if user is_staff and is_active 
     """
    url=reverse('account:api-v1:login')

    def test_user_login(self,api_client,create_user):

        response=api_client.post(self.url,data)
        assert response.status_code==200


    def test_user_login_is_staff_false(self,api_client,create_user):
        """
         if user is not staff 
        """
        create_user=create_user
        create_user.is_staff=False
        create_user.save()

        response=api_client.post(self.url,data)
        assert response.status_code==400

    def test_user_wrong_password(self,api_client,create_user):
        """
            if password is wrong 
        """
        create_user=create_user
        create_user.set_password('123#4567')
        create_user.save()
        response=api_client.post(self.url,data)
        assert response.status_code==400