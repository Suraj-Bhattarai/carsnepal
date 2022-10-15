# from celery.decorators import task
# from celery.utils.log import get_task_logger
# from time import time
# from .views import send_mail_to

# sleeplogger = get_task_logger(__name__)@task(name='send_mail_task')

# def send_mail_task(duration, request):
#     subject= 'Celery'
#     message= 'My task done successfully'
#     receiver= 'receiver_mail@gmail.com'
#     is_task_completed= False
#     error=''

#     try:
#         sleep(duration)
#         is_task_completed= True
#     except Exception as err:
#         error= str(err)
#         logger.error(error)

#     if is_task_completed:
#         send_mail_to(subject, message, receivers)
#     else:
#         send_mail_to(subject, error, receivers)

#     return('Completed')



from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

logger = get_task_logger(__name__)

# @app.task(name='send_email_task')
@shared_task(bind=True)
def send_mail_task(self,subject, message):
    admin_info = User.objects.get(is_superuser=True)
    admin_email = admin_info.email
    send_mail(subject,message,settings.EMAIL_HOST_USER,[admin_email],fail_silently= False)
