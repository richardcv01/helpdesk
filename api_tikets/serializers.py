from django.http import Http404
from rest_framework import serializers
from tikets.models import Tikets, Topic, Implementation
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import get_current_timezone
import pytz

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'topic_text',)

class tikets_idSerializer(serializers.Serializer):
    id = serializers.CharField()

class ImplementationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Implementation
        fields = ('id','implementation_text')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        #fields = ('id', 'email')
        read_only_fields = fields

class UserSerializer_1(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()



class TiketsSerializer(serializers.ModelSerializer):
    tikets_Topic = TopicSerializer()
    tikets_implementation = ImplementationSerializer()
    #tikets_Owner = UserSerializer()
    tikets_Owner = UserSerializer_1()
    class Meta:
        model = Tikets
        fields = ('pk', 'tikets_PIP', 'tikets_email', 'tikets_Phone',
                  'tikets_Location', 'tikets_text', 'tikets_pub_date',
                  'tikets_implementation_date',
                  'tikets_Topic', 'tikets_implementation', 'tikets_Owner')
        #read_only_fields = ("tikets_Owner")


    def create(self, validated_data):
        topic_data = validated_data.pop('tikets_Topic')
        topic_obj = Topic.objects.get(**topic_data)
        Implementation_data = validated_data.pop('tikets_implementation')
        Implementation_obj = Implementation.objects.get(**Implementation_data)
        #user_data = validated_data.pop('tikets_Owner')
        #user_obj = User.objects.get(**user_data)
        users_data = validated_data.pop('tikets_Owner')
        users_obj = User.objects.get(**users_data)
        return Tikets.objects.create(tikets_Topic=topic_obj, tikets_implementation=Implementation_obj, tikets_Owner=users_obj,  **validated_data)
        #return Tikets.objects.create(tikets_Topic=topic_obj, tikets_implementation=Implementation_obj, **validated_data)
        #return Tikets.objects.create(**validated_data)

    def update(self, instance, validated_data):  # Параметр instance получает конкретный экземплярный объект модели validated_data получает десериализованные данные
        "" "Обновить, экземпляр - это экземпляр объекта, который будет обновлен" ""

        Implementation_data = validated_data.pop('tikets_implementation')
        tiket_impl = instance.tikets_implementation
        pk = Implementation_data.get('id')
        Impements = Implementation.objects.get(id=pk)
        instance.tikets_implementation = Impements

        Users_data = validated_data.pop('tikets_Owner')
        user = instance.tikets_Owner
        pk = Users_data.get('id')
        Users = User.objects.get(id=pk)
        instance.tikets_Owner = Users
        #instance.tikets_Owner = validated_data.get('tikets_Owner', instance.tikets_Owner)



        instance.tikets_implementation_date = datetime.now(tz=get_current_timezone())
        #print(datetime)
        instance.save()
        return instance










