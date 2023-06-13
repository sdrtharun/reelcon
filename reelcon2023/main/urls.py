from django.urls import path
from main.views import countdown_timer, update_timer,countdown_api

urlpatterns = [
    path('countdown/', countdown_timer, name='countdown'),
    path('update-timer/', update_timer, name='update_timer'),
    path('countdown/api/', countdown_api, name='countdown_api'),
]