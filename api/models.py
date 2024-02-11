from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField(blank=True)
    subject = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)


# Superuser:
# Username: hilla_nir
# Email: hilla_nir@gmail.com
# Password: hilla_abra
    

# {
# "username" : "check",
# "password" : "nothbook"
# }


# {
#   "sender": {
#     "username": "check"
#   },
#   "receiver": {
#     "username": "example"
#   },
#   "message": "23:58",
#   "subject": "23:58"
# }