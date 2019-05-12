from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished) # django信号
def callback(sender, **kwargs):
    print('sender:',sender)
    print(kwargs)
    print("Request finished!")

