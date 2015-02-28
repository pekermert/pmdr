from timer.models import Users, Teams, Company, TimeRecord
from rest_framework import viewsets
from timer.serializers import UserSerializer, TeamSerializer, CompanySerializer, TimeRecordSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Teams.objects.all()
	serializer_class = TeamSerializer

class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class TimeRecordViewSet(viewsets.ModelViewSet):
	queryset = TimeRecord.objects.all()
	serializer_class = TimeRecordSerializer
