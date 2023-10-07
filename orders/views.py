from django.shortcuts import render
from .models import Order
from customers.models import Customer
from robots.models import Robot
# Create your views here.
from django.views.generic.edit import CreateView
import json
from django.http import JsonResponse


# from django.core.mail import send_mail


class CreateOrder(CreateView):

    def post(self, request, *args, **kwargs):
        try:
            order_json = json.loads(request.body.decode('utf-8'))
            customer_email = order_json['customer']
            robot_serial = order_json['robot_serial']
            customer, created = Customer.objects.get_or_create(
                email=customer_email)
            is_availability = Robot.objects.filter(serial=robot_serial, in_stock=True).exists()  # True

            order = Order(customer=customer, robot_serial=robot_serial)
            # serial,model= Robot.objects.filter(serial=robot_serial).values('version', 'model',
            #                                                                ).distinct()
            # # for entry in distinct_values:
            # #     serial = entry['serial']
            # #     model = entry['model']
            # #     print(f"Serial: {serial}, Model: {model}")
            # print(serial['version'],model['model'])
            if not is_availability:
                order.is_pending = True
                order.save()

                return JsonResponse({'message': 'Your order is added pending'})

            return JsonResponse({'message': 'Your order is created succesfuly '})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
