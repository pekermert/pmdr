from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status

from timer.models import TimeRecord,User
from timer.serializers import TimeRecordSerializer,UserSerializer
from timer.utils import check_timer,remaining_time

	
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
		'''
		Returns the users last timer object
		'''
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
		'''
		Creates new timer
		'''
		try:
			new_data = TimeRecordSerializer(data = request.data)
			print request.data
			if new_data.is_valid():
				new_data.save()
				return Response(new_data.data, status=status.HTTP_201_CREATED)
			return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST)
		except TimeRecord.DoesNotExist: # Error ?? ! 
			return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST) 

	def put(self, request, timer_id=None, *args, **kw):
		'''
		Timer request for DONE or CANCEL status.
		'''
		try:
			if timer_id:
				#timer object for checking
				record = TimeRecord.objects.filter(id=timer_id,status='CT')
				#timer object for update
				dt = TimeRecord.objects.get(id=timer_id,status='CT',owner=request.user.id)
				timer_check = check_timer(record)
				if timer_check:
					dt.status = 'DN' #DONE
					dt.save()
					return Response(status=status.HTTP_200_OK)
				else:
					dt.status = 'CL' #CANCEL
					dt.save()
					return Response({'Error':'Timer Canceled!'}, status=status.HTTP_200_OK)	
			else:
				return Response({'Error':'Timer ID required!'}, status=status.HTTP_400_BAD_REQUEST)
		except TimeRecord.DoesNotExist:
			return Response({'Error':'Record does not exist'}, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response({'Error':'Exception throwing'} , status=status.HTTP_400_BAD_REQUEST)
		
class TimerSyncView(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )
	permission_classes = ()	
	#IsAuthenticated,

	def get(self, request, user_id=None, *args, **kw):
		'''
		Returns the users current timer duration
		'''
		try:
			if user_id is None:
				user_id = request.user.id
			record = TimeRecord.objects.filter(owner=user_id,status="CT").latest('id')
			timer_duration = remaining_time(record)
			return Response({'remaining':timer_duration}, status=status.HTTP_200_OK)
		except TimeRecord.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

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