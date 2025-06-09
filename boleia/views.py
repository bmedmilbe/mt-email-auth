
from django.http import HttpResponse, JsonResponse

from django.core.mail import get_connection, send_mail
from pprint import pprint
import json
from django.views.decorators.csrf import csrf_exempt # For testing, handle CSRF properly in production

def send(request):
    # pprint((request.body))
    if request.method == 'POST':

        try:
            # 1. Access raw body data
            raw_data = request.body

            # 2. Decode bytes to string
            decoded_data = raw_data.decode('utf-8')

            # 3. Parse JSON string into a Python dictionary
            data = json.loads(decoded_data)

            # Now access your data using the dictionary keys
            airport = data.get('airport')
            phone = data.get('phone')
            recipient_list = ["elmerramos@outlook.pt", "edmilbe@gmail.com"]
            subject = f'Viagem {airport}'
            
            message = f'Solicitada uma viagem de/para {airport}. Contacto: {phone}.'
            from_email = 'edmilbe@gmail.com'  
            # Replace with your email address
            send_mail(subject, message, from_email, recipient_list)
            
            print(f"Airport: {airport}, Phone: {phone}")


            # Example response
            return JsonResponse({'message': 'Data received successfully!', 'airport': airport, 'phone': phone})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)
    else:
        return HttpResponse("This view only accepts POST requests.", status=405)

    # contact = "6778988"
    # airport = "hgfh"
    
    # pprint(HttpResponse(request.POST))
    return HttpResponse(request)