from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mahsulot, Client, Stats, Ombor
from .serializers import MahsulotSer, ClientSer, StatsSer, OmborSer


class ClientAPIView(APIView):
    def get(self, request):
        c = Client.objects.get(user=request.user)
        clientlar = Client.objects.filter(profil=c)
        ser = ClientSer(clientlar, many=True)
        return Response(ser.data)
    def post(self, request):
        c = Client.objects.get(user=request.user)
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=c)
        return Response(ser.data)


class MahsulotAPIView(APIView):
    def get(self, request):
        m = Mahsulot.objects.get(user=request.user)
        mahsulotlar = Mahsulot.objects.filter(profil=m)
        ser = MahsulotSer(mahsulotlar, many=True)
        return Response(ser.data)
    def post(self, request):
        m = Mahsulot.objects.get(user=request.user)
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=m)
        return Response(ser.data)
    def update(self, request):
        m = Mahsulot.objects.get(user=request.user)
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=m)
        return Response(ser.data)


class StatsAPIView(APIView):
    def get(self, request):
        s = Stats.objects.get(user=request.user)
        stats = Stats.objects.filter(profil=s)
        ser = StatsSer(stats, many=True)
        return Response(ser.data)


class OmborAPIView(APIView):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        ombor = Ombor.objects.filter(profil=o)
        ser = OmborSer(ombor, many=True)
        return Response(ser.data)

