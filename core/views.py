from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
import requests
import json
from pprint import pprint
# Create your views here.
import logging

logger = logging.getLogger(__name__)


# class HelloView(APIView):)

def say_hello(request):
    try:
        # send_mail('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
        # message.attach_file("core/static/images/contact-us.png")
        # message.send()

        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Mosh Hamedanny'})
        message.attach_file("core/static/images/contact-us.png")
        message.send(['john@bonsmabos.com'])

    except BadHeaderError:
        pass

    return render(request, 'core/hello.html', {'msg': 'Email was successfully sent!'})



@api_view(['GET'])
def my_address(request):
    """
    List all code snippets, or create a new snippet.
    """

    headers = {'Accept': 'application/json'}

    ip = requests.get('http://api.ipify.org?format=json', headers=headers)
   
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/'+ip_data['ip'], headers=headers)

    post_code = ""
    location_data_as = res.text.strip().split('"')
    for i in range(len(location_data_as)):
        if location_data_as[i] == 'zip': 
            post_code = location_data_as[i+2]
    
    return Response({'data':post_code})
   
    

    # return render(request, 'core/hello.html', {'data':location_data})