from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from googletrans import Translator

from home.utilits import audio_file_to_text
from .models import UsedLanguages
from .models import Voice
from translator import settings


def home(request, *args, **kwargs):
    context = {
        "languages": UsedLanguages.objects.all()    
    }
    return render(request, 'text-translate.html', context)


def speak_translate(request, *args, **kwargs):
    context = {
        "languages": UsedLanguages.objects.all()    
    }
    return render(request, 'speak-translate.html', context)


### with googletrans
@api_view(['POST'])
def translate(request):
    if request.method == 'POST':
        
        translator = Translator()
        
        input_text = request.POST.get('text')
        from_language = request.POST.get('from')
        to_language = request.POST.get('to')
        
        if input_text == '':
            content = {'error': 'Empty input!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                translation = translator.translate(text=input_text, src=from_language, dest=to_language)
                # print(f"Translated Word: {translation.text}")
                content = {"output": translation.text }
                return Response(content, status=status.HTTP_200_OK)
            except Exception as e:
                content = {'error': f'Unexpected error! {e}'}
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'error': 'Unexpected error!'})



@api_view(['POST'])
def save_voice(request):
    from_lang = request.POST.get('language')
    to_lang = request.POST.get('tolanguage')
    audio_file = request.FILES.get('audio_file')

    if from_lang and audio_file and to_lang: 
        voice_instance = Voice(audio_file=audio_file) 
        voice_instance.save()  
        file = str(settings.BASE_DIR) + voice_instance.audio_file.url 
        text = audio_file_to_text(file, from_lang, to_lang) 

        return JsonResponse({'success': f'Audio saved successfully: ', 'output': text.text})

    return JsonResponse({'error': 'Invalid request'})


