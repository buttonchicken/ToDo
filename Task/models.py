from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import TASK_STATUS
import uuid

# Create your models here.
class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    task_data = models.CharField(max_length=500)
    status = models.CharField(max_length = 20,choices = TASK_STATUS,default = 'TODO')