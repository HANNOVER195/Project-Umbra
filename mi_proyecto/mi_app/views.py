from django.shortcuts import render
from django.http import JsonResponse
from .firebase import auth  # Asegúrate que firebase.py inicializa firebase_admin correctamente
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Email y contraseña son requeridos'}, status=400)

            user = auth.create_user(email=email, password=password)
            return JsonResponse({'uid': user.uid, 'email': user.email})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def verificar_usuario(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            id_token = body.get('idToken')
            if not id_token:
                return JsonResponse({'status': 'error', 'message': 'idToken es requerido'}, status=400)

            decoded_token = auth.verify_id_token(id_token)  # ← sin clock_skew
            uid = decoded_token['uid']
            return JsonResponse({'status': 'success', 'uid': uid})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=401)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def index(request):
    return render(request, 'login.html')  # Asegúrate de que 'login.html' esté dentro de tu carpeta 'templates'
