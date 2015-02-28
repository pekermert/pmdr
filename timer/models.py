from django.db import models

TEAMLEAD = 'TL'
DEVELOPER = 'DV'
SCRUM = 'SM'
GROUP_CHOICES = (
    (TEAMLEAD, 'Team Lead'),
    (DEVELOPER, 'Developer'),
    (SCRUM, 'Scrum Master'),
)

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

class Users(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.EmailField(primary_key=True)
	passwd  = models.CharField(max_length=100,blank=False)
	groups = models.CharField(max_length=2,choices=GROUP_CHOICES,default=DEVELOPER)
 	
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class TimeRecord(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey('Users')
	start_time = models.DateTimeField(auto_now_add=True)
	types = models.CharField(max_length=2,choices=TIME_CHOICES,default=STUDY)
	team = models.ForeignKey('Teams')
	status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=CONTINUES)
	
	class Meta:
		unique_together = (("user", "start_time"),)


class Teams(models.Model):
	name = models.CharField(primary_key=True,max_length=50,blank=False)
	corp = models.ForeignKey('Company')

	class Meta:
		unique_together = (("name", "corp"),)
		
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Company(models.Model):
	name = models.CharField(primary_key=True,max_length=50,blank=False)
	url = models.URLField()
	owner = models.ForeignKey('Users')

	def __str__(self):              # __unicode__ on Python 2
		return self.name

