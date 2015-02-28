from timer.models import Users, Teams, Company, TimeRecord
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('name','email','groups')

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teams
		fields = ('name', 'corp')

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name','url','owner')

class TimeRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimeRecord
		fields = ('id','user','start_time','types','team','status')