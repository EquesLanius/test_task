from rest_framework import generics
from .models import User
from .serializers import UserSerializer



# Представление для создания нового пользователя
class CreateUserAPI(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer


# Представление для получения пользователя по его id
class GetUserAPI(generics.ListAPIView):
     serializer_class = UserSerializer

     def get_queryset(self):
          pk = self.kwargs.get("pk")
          if not pk:
               return User.objects.all()
          
          return User.objects.filter(pk=pk)