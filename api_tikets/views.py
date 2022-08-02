from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from celery.result import ResultBase
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from helpdesk import task
from tikets.models import Tikets, Topic, Implementation
from .serializers import TiketsSerializer, TopicSerializer, ImplementationSerializer, UserSerializer, UserSerializer_1, tikets_idSerializer
from rest_framework.serializers import ValidationError
#from datetime import datetime
from dateutil import parser



class tiket_id(APIView):
    def get(self, request):
        try:
            id_tiket = Tikets.objects.all().last()
            print(id_tiket)
            serializer = tikets_idSerializer(id_tiket)
            print('tiket_id', id_tiket)
            return Response({"tiket_id": serializer.data['id']})
        except ObjectDoesNotExist as E:
            print(E)

class TiketsDetail(APIView):
    def get(self, request, pk):
        try:
            tikets = Tikets.objects.get(pk=pk)
            serializer = TiketsSerializer(tikets)
            return Response({"tikets": serializer.data})
        except ObjectDoesNotExist as E:
            print(E)

    def post(self, validated_data):
        return Tikets.objects.create(**validated_data)


    @csrf_exempt
    #@method_decorator(csrf_exempt, name='dispatch')

    def put(self, request, pk):
        tikets = None
        try:
            tikets = Tikets.objects.get(pk=pk)
        except Tikets.DoesNotExist as E:
            print(E)
        print('pk ',pk)
        print('tikets=', tikets)
        if tikets:
            serializer = TiketsSerializer(instance=tikets, data=request.data, partial=True)
            #serializer = TiketsSerializer(tikets, data=data)
            print('DATA', serializer.initial_data)
            print('!!!!!!!!!!!!')
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            print('тікет не існує')
            return Response(status=status.HTTP_400_BAD_REQUEST)

#@method_decorator(login_required, name='dispatch')

class TiketsList(APIView):
    @method_decorator(login_required)
    def get(self, request):
        print('EEEEEEE')
        tikets = Tikets.objects.all()
        serializer = TiketsSerializer(tikets, many=True)
        return Response({"tikets": serializer.data})

    def post(self, request):
        tiket = request.data.get('tikets')
        #print('tiket1', tiket)
        #task.bot_run("ПІП: ", tiket['tikets_PIP'],
                    # "\nДата заявки", tiket['tikets_PIP'] )
        # Create an article from the above data
        serializer = TiketsSerializer(data=tiket)
        print("!!!!!!!!! serializer = ", serializer)
        #if serializer.is_valid(raise_exception=True):
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        else:
            #print('111')
            tikets_saved = serializer.save()
            #tprint('222 ', serializer.data)
            date = serializer.data['tikets_pub_date']
            datef = parser.parse(date)
            dateff = str(datef.day) + "." + str(datef.month) + "." + str(datef.year) + " " + str(datef.hour) + ':' + str(datef.minute)

            task.tel_bot_send.delay("------ НОМЕР ЗАЯВКИ: "+ str(serializer.data['pk'])+ "-------\n" +
                               "\nДата заявки: " + dateff +
                               "\nЗміст заявки: " + serializer.data['tikets_text']
                               )

            #task.add.delay(2, 2)

            task.bot_run.delay(("------ НОМЕР ЗАЯВКИ: "+ str(serializer.data['pk'])+ "-------\n" +
             "ПІП: "+ serializer.data['tikets_PIP']+
            "\nДата заявки: "+ dateff +
            "\nНомер телефону: " + serializer.data['tikets_Phone'] +
            "\nЗміст заявки: " +   serializer.data['tikets_text']
                  ))

            #task.bot_run.delay('1')
            #task.bot_run().apply_async(("@",))
            #task.bot_run(("ПІП: "+ serializer.data['tikets_PIP']))
            #r = task.pr(x=1)
            #result = task.bot_run.delay("HELLO")
            #bot.run("HELLLO@@@")
            #celery.endure_ten_seconds()
        return Response({"success": "Tiket '{}' created successfully".format(tikets_saved.tikets_PIP)})


class TopicView(APIView):

    def get(self, request):
        topics = Topic.objects.all()
        print(topics)
        serializer = TopicSerializer(topics, many=True)
        print(serializer.data)
        return Response({"topic_text": serializer.data})


class InplementionView(APIView):

    def get(self, request):
        inplemention = Implementation.objects.all()
        #print(inplemention)
        serializer = ImplementationSerializer(inplemention, many=True)
        #print(serializer.data)
        return Response({"implementation_text": serializer.data})

class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        #print(inplemention)
        serializer = UserSerializer_1(users, many=True)
        #print(serializer.data)
        return Response({"username": serializer.data})

class UserDetail(APIView):
    def get(self, request, username):
        try:
            user_ = User.objects.get(username=username)
            serializer = UserSerializer(user_)
            return Response({"user_": serializer.data})
        except ObjectDoesNotExist as E:
            print(E)

class UserNameID(APIView):
    def get(self, request, pk):
        try:
            username = User.objects.get(pk=pk)
            print(pk)
            serializer = UserSerializer_1(username)
            return Response({"username": serializer.data})
        except ObjectDoesNotExist as E:
            print(E)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def send_user_ajax(request):
    #if request.is_ajax():
    if is_ajax(request=request):
        dic_user = {}
        if request.user.is_authenticated:
            dic_user['id'] = request.user.id
            dic_user['username'] = request.user.username
            return JsonResponse(dic_user)
        else:
            dic_user['id'] = None
