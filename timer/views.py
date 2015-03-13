from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from timer.models import TimeRecord,User
from timer.serializers import TimeRecordSerializer,UserSerializer

class TodayList(APIView):
	'''
	List of todays pomodoros
	'''
	def get(self, request, format=None):
		d = datetime.datetime.now()
		datenow = "%s-%s-%s" % (d.year, d.month, d.day)
		pomodoroList = TimeRecord.objects.filter(on_date=datenow)
		serializer   = TimeRecordSerializer(pomodoroList, many=True)
		return Response(serializer.data , status=status.HTTP_200_OK)

class UserView(APIView):
	'''authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()
'''
	def get(self, request, format=None):
		'''data = {
			'id': request.user.id,
			'username': request.user.username,
			'token': str(request.auth)
		}
		return Response(data)
		'''
		userList = User.objects.all()
		serializer = UserSerializer(userList, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
		

class RegisterView(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()

	def post(self, request, format=None):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class TimerView(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		timers = TimeRecord.objects.filter(owner=request.user.id)
		serializer = TimeRecordSerializer(timers,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	def post(self, request, format=None):
		record = TimeRecordSerializer(data = request.data)
		if record.is_valid():
			record.save()
			return Response(record.data, status=status.HTTP_201_CREATED)
		return Response(record.errors, status=status.HTTP_400_BAD_REQUEST)
		
class UserStatsView(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = (IsAuthenticated,)	

	def get(self, request, format=None):
		timers = TimeRecord.objects.filter(owner=request.user.id)
		serializer = TimeRecordSerializer(timers,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)