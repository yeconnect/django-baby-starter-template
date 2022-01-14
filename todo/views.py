from django.http import HttpResponse
import time
def wait_a_second(request):
    time.sleep(1)
    return HttpResponse('1秒待った')