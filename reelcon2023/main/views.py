from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Countdown
from django.http import JsonResponse
@login_required
def countdown_timer(request):
    countdown = Countdown.objects.first()
    now = timezone.now()
    time_remaining = countdown.end_time - now if countdown else None
    return render(request, 'main/countdown.html', {'time_remaining': time_remaining})

def update_timer(request):
    end_time = timezone.now() + timezone.timedelta(days=1)
    countdown = Countdown.objects.first()
    if countdown:
        countdown.end_time = end_time
        countdown.save()
    else:
        Countdown.objects.create(end_time=end_time)
    return redirect('countdown')
def countdown_api(request):
    countdown = Countdown.objects.first()
    now = timezone.now()
    time_remaining = countdown.end_time - now if countdown else None
    return JsonResponse({'time_remaining': str(time_remaining)})