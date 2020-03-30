from .models import User, Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model=User
    fields = ('id','name','surname','facebook_id','is_sms_verified',)
    read_only_fields = ('created','updated')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','user','email','birthday','bio','points')
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(ProfileSerializer, self).to_representation(instance)