from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .models import CustomUser

@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    if CustomUser.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = CustomUser.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user_id": user.id
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user_id": user.id
    }, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_admin(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, is_admin=True)
    refresh = RefreshToken.for_user(user)
    
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user_id": user.id
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def promote_to_admin(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_admin = True
        user.save()
        return Response({"message": f"{user.username} has been promoted to Admin."}, status=200)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=404)