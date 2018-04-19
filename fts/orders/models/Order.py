from django.db import models
from .Direction import Direction, Urgency, Status
from registration.models import Client
from translator.models import Translator
from ..utils.Utils import validate_file_extension

class Order(models.Model):

    o_id     = models.CharField (max_length = 15, unique=True)
    lang     = models.CharField (max_length = 50)
    pages    = models.CharField (max_length = 5)
    date     = models.CharField (max_length = 20)
    price    = models.CharField (max_length = 15)
    direction = models.ManyToManyField(Direction)
    urgency = models.ForeignKey(Urgency, on_delete=models.CASCADE,  null=True, blank=True)
    customer = models.ForeignKey(Client, on_delete=models.CASCADE,  null=True, blank=True)
    translated = models.OneToOneField(Translator, on_delete=models.CASCADE,  null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,  null=True, blank=True)
    file = models.FileField(upload_to="orders_files/"+str(o_id), validators=[validate_file_extension])

    @property
    def full_title(self):
        return '{0.o_id} {0.lang} {0.pages} {0.urgency} {0.price} {0.customer} {0.translator} {0.status}'.format(self)


    def __str__(self):
        return '{0.o_id} {0.lang} {0.price} {0.urgency} {0.status}'.format(self)
