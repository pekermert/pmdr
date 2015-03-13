from timer.models import TimeRecord, User
from rest_framework import serializers

class TimeRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimeRecord
		fields = ('id','owner','on_date','on_time','types','status')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','first_name','last_name','is_superuser','password','last_login')
	
	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user