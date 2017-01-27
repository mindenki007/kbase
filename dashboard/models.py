from django.db import models
from django.utils import timezone

# Create your models here.
class CIR(models.Model):
    name_of_change = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    author_email_address = models.EmailField(max_length=100)
    contact = models.CharField(max_length=40)
    summary = models.TextField()
    delivery_date = models.DateField()
    channels = models.CharField(max_length=10)
    brands = models.CharField(max_length=40)
    business_area = models.CharField(max_length=40)
    allocated_date = models.DateField(editable=False, auto_now=True)
    allocated_to = models.ForeignKey('auth.User', default=0)
    allocated = models.BooleanField(default=False)
    point = models.IntegerField()
    raised = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name_of_change

class Clockwork(models.Model):
    name_of_change = models.CharField(max_length=100)
    author = models.CharField(max_length = 40)
    author_email_address = models.EmailField(max_length=100)
    contact = models.CharField(max_length=40)
    summary = models.TextField()
    delivery_date = models.DateField()
    channels = models.CharField(max_length=10)
    brands = models.CharField(max_length=40)
    business_area = models.CharField(max_length=40)
    status = models.CharField(max_length=10)
    raised = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name_of_change

class Changes(models.Model):
    name_of_change = models.CharField(max_length=100)
    BRS_num = models.IntegerField()
    author = models.CharField(max_length = 40)
    author_email_address = models.EmailField(max_length=100)
    contact = models.CharField(max_length=40)
    summary = models.TextField()
    delivery_date = models.DateField()
    channels = models.CharField(max_length=10)
    brands = models.CharField(max_length=40)
    business_area = models.CharField(max_length=40)
    allocated_date = models.DateField(editable=False, auto_now=True)
    allocated = models.CharField(max_length=40)
    point = models.IntegerField()
    STATUS = (
        ('op', 'Open'),
        ('st', 'Started'),
        ('im', 'Implemented'),
        ('ab', 'Abadonded'),
        ('ho', 'On Hold')
    )
    status = models.CharField(max_length=10, default='Open', choices=STATUS)

    raised = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name_of_change

class Updates(models.Model):
    change = models.ForeignKey('dashboard.Changes', related_name='up_BRS_num')
    name = models.ForeignKey('dashboard.Changes', related_name='up_author')
    status = models.ForeignKey('dashboard.Changes', related_name='up_status')
    what = models.TextField()
    when = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.what

class Queries(models.Model):
    change = models.ForeignKey('dashboard.Changes', related_name='qu_BRS_num')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title

class Answers(models.Model):
    query = models.ForeignKey('dashboard.Queries', related_name='ans_title')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Defects(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    opened = models.BooleanField(default=True)
    hold = models.BooleanField(default=False)
    inprogress = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    def put_hold(self):
        self.opened = False
        self.hold = True
        self.inprogress = False
        self.closed = False
        self.save()

    def put_progress(self):
        self.opened = False
        self.hold = False
        self.inprogress = True
        self.closed = False
        self.save()

    def close(self):
        self.opened = False
        self.hold = False
        self.inprogress = False
        self.closed = True
        self.save()

    def __str__(self):
        return self.title
