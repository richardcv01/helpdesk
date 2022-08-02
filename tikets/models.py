from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Topic(models.Model):
    topic_text = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_text

class Implementation(models.Model):
    implementation_text = models.CharField(max_length=200)

    def __str__(self):
        return self.implementation_text


class Tikets(models.Model):
    tikets_PIP = models.CharField(max_length=200)
    tikets_email = models.EmailField(max_length = 254)
    tikets_Phone = PhoneNumberField(null=False, blank=False)
    tikets_Location = models.CharField(max_length=200)
    tikets_text = models.CharField(max_length=200)
    tikets_pub_date = models.DateTimeField(auto_now_add=True)
    tikets_implementation_date = models.DateTimeField(null=True)
    #tikets_Owner_date = models.DateTimeField(null=True)
    tikets_Topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=0)
    tikets_implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE, default=1)
    #tikets_Owner = models.ForeignKey(User, verbose_name='Відповідальний', on_delete=models.CASCADE, default=2)
    tikets_Owner = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return str(self.id)





