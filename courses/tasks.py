from celery import shared_task
from icecream import ic
from django.core.mail import EmailMessage
from courses.models import Course
from datetime import date, timedelta
import logging

logger = logging.getLogger(__name__)


@shared_task
def exam_notification():
    try:
        today = date.today()
        course_exam_today = Course.objects.filter(exam_date=today)
        for exam in course_exam_today:
            _email_list = []
            _teacher_email = exam.teacher.user.email
            if _teacher_email:
                _email_list.append(_teacher_email)
            _student_emails = list(exam.students.values_list('user__email', flat=True))
            if _student_emails:
                _email_list.extend(_student_emails)
            print(_email_list)
            for _receiver in _email_list:
                _email_subject = f'{exam.name} exam on {exam.exam_date}'
                _email_body = f'Dear {_receiver}, you have {exam.name} exam on {exam.exam_date}, be prepared.'
                email = EmailMessage(
                    _email_subject, _email_body, None, [f'{_receiver}'])
                try:
                    email.send()
                    logger.info(email.body)
                except Exception as e:
                    ic(e)
                    logger.warning('Sender email not configured, printing the email body in the console instead')
                    logger.info(f'Email subject: {email.subject}')
                    logger.info(f'Email body: {email.body}')

    except Exception as e:
        ic(e)
