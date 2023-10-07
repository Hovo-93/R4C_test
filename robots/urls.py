from django.urls import path
from robots.views import RobotCreateView,UploadExelView

app_name = 'robots'

urlpatterns = [

    path('add_robot/', RobotCreateView.as_view(), name='add_robot'),
    path('download_exel/', UploadExelView.as_view(), name='download_exel'),

]
