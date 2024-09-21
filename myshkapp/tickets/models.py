
import uuid
from django.db import models
from users.models import User

class ticket(models.Model):
    statusch=(
        ('Active','Active'),
        ('Completed','Completed'),
        ('Pending', 'Pending')
    )
    ticket_nu= models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    created_by =models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    date_created= models.DateTimeField(auto_now_add=True)
    assinged_to = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)
    isresolved= models.BooleanField(default=False)
    accepted_date= models.DateTimeField(null=True, blank=True)
    closed_date= models.DateTimeField(null=True, blank=True)
    ticket_stat = models.CharField(max_length=100)

def _str_(self):
    return self.title