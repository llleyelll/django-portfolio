from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return "Email from " + self.email
