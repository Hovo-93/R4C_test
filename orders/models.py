from django.db import models

from customers.models import Customer
from django.db.models.signals import post_save
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)#email
    robot_serial = models.CharField(max_length=5, blank=False, null=False)#roboti serian
    is_pending = models.BooleanField(default=False)  # в ожидании


    def __str__(self):
        return f'Customer:{self.customer} -- order -- Robot:{self.robot_serial}'

    # def ready(self):
    #     post_save.connect(send_order_notification_dispatcher,sender=Order)
# 1usere json-ov kxrge zakaz email robot serial
# 2 robot serialov knaem ete ka roboti modeli mej u in_stoch == false uremn is pendinge orderi meji kdarcnem true
# 3 email kxrgem
# 4 stugel ete v nalichii mej haytnvav u inqe v



#1 naem ete orderi is poending true iran qcem email pendingi mej
#2 fram email-i pending masivi mej u amen xrgem mail
#3 function unenam vornor kstuge maili []ic sax xrvele te che u cron u amen ropen mek stuge
