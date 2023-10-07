import os

from .models import Order
from robots.models import Robot
from django.core.mail import send_mail
from R4C.celery import app
from dotenv import load_dotenv

load_dotenv()

@app.task
def check_robot_is_availability():
    """
     Проверка робота в наличии
    :return:
    """
    for order in Order.objects.filter(is_pending=True):
        is_availability = Robot.objects.filter(serial=order.robot_serial, in_stock=True).exists()
        print(is_availability)
        return is_availability


@app.task
def send_order_notification():
    """
        Функция которое отправляет уведомление клиенту
    :return:
    """
    for order in Order.objects.filter(is_pending=True):
        if order.is_pending:

            if check_robot_is_availability():
                serial, model = Robot.objects.filter(serial=order.robot_serial).values('version', 'model',
                                                                                 ).distinct()

                subject = 'Ваш заказ'
                message = f"Добрый день!Недавно вы интересовались нашим роботом модели " \
                          f"{model['model']}, версии {serial['version']}.Этот робот теперь в наличии.\
                                 Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"
                from_email = os.getenv('FROM_EMAIL')
                recipient_list = [order.customer.email]
                print(recipient_list)
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
