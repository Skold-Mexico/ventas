from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from backend.envio import enviar_correo  # importar tu función

@csrf_exempt
def api_enviar_correo(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Recibe el correo y opcionalmente otros datos
        correo = data.get('correo')
        nombre = data.get('nombre', 'Usuario')
        vencimiento = data.get('vencimiento', '2025-07-31')

        if not correo:
            return JsonResponse({'error': 'Correo no proporcionado'}, status=400)

        if enviar_correo(correo, nombre, vencimiento):
            return JsonResponse({'mensaje': 'Correo enviado correctamente'})
        else:
            return JsonResponse({'error': 'Error al enviar el correo'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
