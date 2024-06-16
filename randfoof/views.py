from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse

from randfoof.models import Restaurent
from randfoof.serializers import *
import randfoof.parser

# Create your views here.
class RestaurentParseAPIView(APIView):
    def get(self, request):
        restaurent = Restaurent.objects.all()
        return Response({'restaurents':""})
    def post(self,request):
        geoData= request.data
        restaurents = Restaurent.objects.all()
        print(request.data)
        hrt = randfoof.parser.parse(geoData["shirota"], geoData["dolgota"])
        responseData = []
        for restaurent in hrt.keys():
            restname= restaurent.split("|")[0]
            print(restaurent.split("|"))
            restpic = restaurent.split("|")[1]
            if restname in [i.name for i in restaurents]:
                responseData.append(Restaurent.objects.get(name=restname))
                continue
            newRestaurent = Restaurent.objects.create(
                name = restname,
                picture = restpic,
                latitude = 12.00,
                longitude = 13.00
            )
            for dish in hrt[restaurent]:
                newPrice = 0
                newDescription = ""
                newPicture = ""
                for param in dish:
                    try:
                        newPrice = int(param)
                        break
                    except:
                        continue
                newDish = Dish.objects.create(
                    name = dish[0],
                    price = newPrice,
                    description = newDescription,
                    picture = newPicture,
                    restaurent = newRestaurent
                )
            responseData.append(newRestaurent)
        return Response({'restaurents':RestaurentSerializer(responseData, many=True).data})

class RestaurentViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Restaurent.objects.all()
    serializer_class = RestaurentSerializer

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class HistoryViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class DishViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer