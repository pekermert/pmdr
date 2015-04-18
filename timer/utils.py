from timer.serializers import TimeRecordSerializer,UserSerializer
from timer.models import TimeRecord,User
import datetime
import string

def check_timer(timer):
	serializer = TimeRecordSerializer(timer, many=True)
	timer_record = serializer.data[0].items()
	#OrderedDic Items Handling
	owner = timer_record[1][1]
	on_date = timer_record[2][1]
	timer_type = timer_record[3][1]
	timer_status = timer_record[4][1]

	#Timer Duration as second
	duration = __type_seconds(timer_type)
	
	#Current time for crosscheck timer validation
	crr_time = datetime.datetime.now()
	on_date_utc_obj = __from_utc(on_date)
	timer_test = __subtract_utc_boolean(crr_time,on_date_utc_obj,duration)
	
	return timer_test

def __type_seconds(timer_type):
	'''
	Returns timer duration as seconds
	'''
	try:
		if timer_type is 'ST': #Study
			sec = 25*60
		elif timer_type is 'SB': #Short Break
			sec = 5*60
		elif timer_type is 'LB': #Long Break
			sec = 30*60
		else:
			sec = 'hata'
		return int(sec)
	except ValueError:
		print 'Timer type Error!'

def __from_utc(utcTime):
	'''
	Converts the input string time to the utc objects
	'''
	return datetime.datetime.strptime(utcTime, "%Y-%m-%dT%H:%M:%S.%fZ")

def __subtract_utc_boolean(date_1,date_2,dist):
	'''
	Calculates distance between the two dates and checks for expected distance.
	'''
	result = (date_1 - date_2).total_seconds()
	if result > dist:
		return True
	else:
		return False

def __subtract_utc(date_1,date_2):
	'''
	Calculates distance between the two dates and returns total seconds
	'''
	result = (date_1 - date_2).total_seconds()
	return result

def remaining_time(time):
	serializer = TimeRecordSerializer(time)
	timer_record = serializer.data.items()

	owner = timer_record[1][1]
	on_date = timer_record[2][1]
	timer_type = timer_record[3][1]
	timer_status = timer_record[4][1]

	duration = __type_seconds(timer_type)
	crr_time = datetime.datetime.now()
	on_date_utc_obj = __from_utc(on_date)
	
	remaining = __subtract_utc(crr_time,on_date_utc_obj)
	print duration
	print remaining
	result = duration - remaining

	return result

### CHECK for USER CT TIMERS ###

def ct_timer_check(user_id):
	last_record = TimeRecord.objects.filter(owner=user_id,status='CT')
