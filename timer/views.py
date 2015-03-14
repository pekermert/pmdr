from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from timer.models import TimeRecord,User
from timer.serializers import TimeRecordSerializer,UserSerializer

	
class UserProfileView (APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()

	def get(self, request, user_id=None, *args, **kw):
		#get_arg1 = request.GET.get('arg1', None)
		if user_id is None:
			user_id = request.user.id
		user = User.objects.filter(id=user_id)
		serializer = UserSerializer(user,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	#TODO : put method = Update profile

class TimeRecordView (APIView):	
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()

	def get(self, request, user_id=None, *args, **kw):
		try:
			if user_id is None:
				user_id = request.user.id
			last_record = TimeRecord.objects.filter(owner=user_id).latest('id')
			serializer = TimeRecordSerializer(last_record,many=False)
			#Check Latest Record validity
			#Add modifier for ST SB LB
			#Add modifier for status DN CT CL
			return Response(serializer.data, status=status.HTTP_200_OK)
		except TimeRecord.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def post(self, request):
		try:
			new_data = TimeRecordSerializer(data = request.data)
			if new_data.is_valid():
				new_data.save()
				return Response(new_data.data, status=status.HTTP_201_CREATED)
			return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST)
		except TimeRecord.DoesNotExist: # Error ?? ! 
			return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST) 

	#TODO : put method = Update state timer DONE , RESET
	def put(self, request, timer_id=None, *args, **kw):
		try:
			timer_status = request.GET.get('status', None)
			if timer_id:
				if timer_status:
					# THERE IS NOT OK    !!!!!!!!!!!!
					record = TimeRecord.objects.filter(id=timer_id,owner=request.user.id) \
					.update(status=timer_status)
			else:	
				return Response(status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		
class UserStatsView(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()	
	#IsAuthenticated,
	def get(self, request, user_id=None, *args, **kw):
		#timers = TimeRecord.objects.filter(owner=request.user.id)
		status_arg = request.GET.get('status', None)
		if status_arg:
			timers = TimeRecord.objects.filter(owner=user_id,status=status_arg)
		else:
			timers = TimeRecord.objects.filter(owner=user_id)
		# Add types condition
		serializer = TimeRecordSerializer(timers,many=True)
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