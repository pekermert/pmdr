from django.contrib.auth.models import User
from django.db import models

STUDY = 'ST'
SHORT_BREAK = 'SB'
LONG_BREAK = 'LB'
TIME_CHOICES = (
	(STUDY, 'Study Time'),
	(SHORT_BREAK, 'Short break'),
	(LONG_BREAK, 'Long break'),
)

DONE = 'DN'
CANCEL = 'CL'
CONTINUES = 'CT'
STATUS_CHOICES = (
	(DONE, 'Done'),
	(CANCEL, 'Canceled'),
	(CONTINUES, 'Contuniues'),
)

class TimeRecord(models.Model):
	id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(User)
	on_date = models.DateTimeField(auto_now_add=True)
	types = models.CharField(max_length=2,choices=TIME_CHOICES,default=STUDY)
	status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=CONTINUES)
