import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# import translators as ts
from googletrans import Translator
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




# text translate and send to html with class
# class TextTranslateView(TemplateView):
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