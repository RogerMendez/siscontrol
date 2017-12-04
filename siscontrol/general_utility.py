#encoding:utf-8
from django.core.mail import EmailMultiAlternatives
from django.contrib.contenttypes.models import ContentType

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.conf import settings

import os

import random
import threading
from datetime import time
import time

from django.http import HttpResponse

import ho.pisa as pisa
import cStringIO as StringIO
import cgi

def create_code_activation():
    #li = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0']
    li = ['1','2','3','4','5','6','7','8','9','0']
    #51 elementos
    code = random.choice(li)
    for i in range(4):
         code += random.choice(li)
    return code


def send_email(email, html, subject = 'Codigo De Activacion'):
    text_content = 'Mensaje...nLinea 2nLinea3'
    html_content = html
    from_email = '"Prospection" <sieboliva@gmail.com>'
    to = email
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    #send_mail('Subject here', html, 'from@example.com', [], fail_silently=False)


def admin_log_addition(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = u'%s'%objecto,
                action_flag     = ADDITION,
                change_message = mensaje,
            )

def admin_log_change(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = u'%s'%objecto,
                action_flag     = CHANGE,
                change_message = mensaje,
            )

def generar_pdf(html):
    result = StringIO.StringIO()
    links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-16")), dest=result, link_callback=fetch_resources)
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def fetch_resources(uri, rel):
    import os.path
    BASE_DIR = settings.BASE_DIR
    path = os.path.join(
            os.path.join(BASE_DIR, 'static'),
            uri.replace(settings.STATIC_URL, ""))
    return path

def restar_horas(hora1, hora2):
    #hora1 - hora2
    h1 = int(hora1[0:2])
    h2 = int(hora2[0:2])
    m1 = int(hora1[3:5])
    m2 = int(hora2[3:5])
    h = h1 - h2
    m  = m1 - m2
    if m < 0:
        m = m + 60
        h -= 1
    if m < 10:
        min = "0" + str(m)
    else:
        min = str(m)
    if h < 10 :
        hr = "0" + str(h)
    else:
        hr = str(h)
    return str(hr) + ":" + str(min)

def sumar_horas(hora1, hora2):
    h1 = int(hora1[0:2])
    h2 = int(hora2[0:2])
    m1 = int(hora1[3:5])
    m2 = int(hora2[3:5])
    h = h1 + h2
    m  = m1 + m2
    if m >= 60:
        m = m - 60
        h += 1
    if m < 10:
        min = "0" + str(m)
    else:
        min = str(m)
    if h < 10 :
        hr = "0" + str(h)
    else:
        hr = str(h)
    return str(hr) + ":" + str(min) + ":00"