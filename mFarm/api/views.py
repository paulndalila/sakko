from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from mFarm.api.serializers.Serializers import FarmerSerializer, SaccoSerializer, ChangePasswordSerializer, \
    UpdateUserSerializer
from mFarm.models import Farmer, Sacco


@api_view(http_method_names=['GET'])
def apiRoutes(request):
    routes = [
        "api/login",
        "api/login/refresh",
        "api/signup",
        "api/farmers",
        "api/farmer<pk:str>"
    ]
    return Response(data=routes)


#  get all farmers
# @login_required(login_url='index')
@api_view(http_method_names=['GET'])
def getFarmers(request):
    farmers = Farmer.objects.all()
    serializer = FarmerSerializer(farmers, many=True)
    return Response(data=serializer.data)


# add a new farmer
@api_view(http_method_names=['POST'])
def addFarmer(request):
    if request.method == 'POST':
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response(data=serializer.data)


@api_view(http_method_names=['GET'])
def getFarmer(request, pk):
    farmer = Farmer.objects.get(id=pk)
    serializer = FarmerSerializer(farmer, many=False)
    return Response(data=serializer.data)


@api_view(http_method_names=['POST'])
def updateFarmer(request, pk):
    farmer = Farmer.objects.get(id=pk)
    serializer = FarmerSerializer(instance=farmer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data)


@api_view(http_method_names=['DELETE'])
def deleteFarmer(request, pk):
    farmer = Farmer.objects.get(id=pk)
    farmer.delete()
    return Response(data="Farmer deleted successfully")


@api_view(http_method_names=['POST'])
def createSaco(request):
    sacco = SaccoSerializer(data=request.data)
    if sacco.is_valid(raise_exception=True):
        sacco.save()
    else:
        return Response(data=sacco.errors)
    return Response(data="Sacco created successfully", status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET'])
def getSacco(request):
    sacco = Sacco.objects.all()
    serializer = SaccoSerializer(sacco, many=True)
    return Response(data=serializer.data)


# signup endpoint
@api_view(http_method_names=['POST'])
def signup(request):
    user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
    user.save()
    return Response(data="User created successfully")


# login endpoint
@api_view(http_method_names=['POST'])
def login(request):
    user = User.objects.get(username=request.data['username'])
    if user.check_password(request.data['password']):
        return Response(data="User logged in successfully", status=status.HTTP_200_OK)
    else:
        return Response(data="Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)


# logout endpoint
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
