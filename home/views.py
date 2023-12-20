import json
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# import translators as ts
from googletrans import Translator

from home.utilits import audio_file_to_text
from .models import UsedLanguages
from django.views.generic.base import TemplateView


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
# class HomePageView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(self.request.GET.get('page'))
#         page = self.request.GET.get('page')
#         if page:
#             context['page'] = page
#         else:
#             context['page'] = 'text-translate'
#         context['languages'] = UsedLanguages.objects.all()
#         return context


# @api_view(['POST'])
# # @csrf_exempt  
# def speak_translate(request):  
#     wavfile=request.FILES['wavfile']  
#     #logic of your wav file what you want to do 
#     return JsonResponse(status=200,data={'success':'success'},safe=False)  




### with googletrans
@api_view(['POST'])
def translate(request):
    if request.method == 'POST':
        
        translator = Translator()
        
        input_text = request.POST.get('text')
        from_language = request.POST.get('from')
        to_language = request.POST.get('to')
        
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


from .forms import VoiceForm
from .models import Voice
import soundfile

@api_view(['POST'])
def save_voice(request):
    from_lang = request.POST.get('language')
    to_lang = request.POST.get('tolanguage')
    audio_file = request.FILES.get('audio_file')
    print(from_lang)
    print(to_lang)
    print(audio_file)
    # print(request.FILES)

    if from_lang and audio_file and to_lang: 
        # Assuming you already have a Voice model instance 
        voice_instance = Voice(audio_file=audio_file) 
        voice_instance.save()     
        file = "/home/ProLinux/Documents/GitHub/real-time-translator" + voice_instance.audio_file.url 
        print(file) 
        text = audio_file_to_text(file, from_lang, to_lang) 

        return JsonResponse({'success': f'Audio saved successfully: ', 'output': text.text})

    return JsonResponse({'error': 'Invalid request'})

    # return render(request, 'save_voice.html', {'form': form})




# from speech_recognition import Recognizer, Microphone, AudioFile
# import base64
# from .models import AudioModel
# r = Recognizer()
# mic = Microphone()

# def TTSHome(request):
#     # return render(request, 'tts.html')
#     if request.ajax:
#         print(request.POST.get('datas'))
#         print(request.FILES.get('datas'))
        
#         return JsonResponse({'success': 'Audio saved successfully'})
    
#     if request.POST:
#         file = request.FILES.get('file')
#         lang = request.POST.get('lang')
#         dlang = request.POST.get('dlang')
        
#         audio_obj = AudioModel()
#         audio_obj.audioname = "test1"
#         audio_obj.audio = file
#         audio_obj.save()
#         print("file saved successfully")
        
    
#     return JsonResponse({'error': 'Invalid request'})
    