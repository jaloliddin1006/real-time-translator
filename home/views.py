import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# import translators as ts
from googletrans import Translator
from .models import UsedLanguages

def home(request):
    context = {
        "languages": UsedLanguages.objects.all()    
    }
    return render(request, 'home.html', context)


#### with translators
# @api_view(['POST'])
# def translate(request):
#     if request.method == 'POST':
#         input = json.loads(request.body.decode('utf-8'))['input']
#         from_language = json.loads(request.body.decode('utf-8'))['from']
#         to_language = json.loads(request.body.decode('utf-8'))['to']
#         if input == '':
#             content = {'error': 'Empty input!'}
#             return Response(content, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             output = ts.translate_text(
#                 input, from_language=from_language, to_language=to_language)
#             content = {'output': output}
#             return Response(content, status=status.HTTP_200_OK)
#     return JsonResponse({'error': 'Unexpected error!'})




#### with googletrans
@api_view(['POST'])
def translate(request):
    if request.method == 'POST':
        
        translator = Translator()
        
        input_text = json.loads(request.body.decode('utf-8'))['input']
        from_language = json.loads(request.body.decode('utf-8'))['from']
        to_language = json.loads(request.body.decode('utf-8'))['to']
        
        # print(f"Input: {input_text}")
        # print(f"From: {from_language}")
        # print(f"To: {to_language}")
        
        if input_text == '':
            content = {'error': 'Empty input!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                translation = translator.translate(text=input_text, src=from_language, dest=to_language)
                # print(f"Translated Word: {translation.text}")
                content = {
                    "output": translation.text}
               
                return Response(content, status=status.HTTP_200_OK)
            except Exception as e:
                content = {'error': f'Unexpected error! {e}'}
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'error': 'Unexpected error!'})