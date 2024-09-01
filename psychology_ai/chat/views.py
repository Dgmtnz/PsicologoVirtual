# chat/views.py

import os
import replicate
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation, Message

os.environ["REPLICATE_API_TOKEN"] = "r8_IGGtz9rUgMViUtUhX9ulweKkCMPE04q3RgSC3"

def home(request):
    return render(request, 'chat/home.html')

def end_day(request):
    if request.method == 'POST':
        conversation_id = request.POST.get('conversation_id')
        conversation = Conversation.objects.get(id=conversation_id)
        messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
        
        summary = generate_summary(messages)
        
        # Guardar el resumen en un archivo
        user_folder = f'memory/user_{conversation.user.id}'
        os.makedirs(user_folder, exist_ok=True)
        with open(f'{user_folder}/context.txt', 'a') as f:
            f.write(f"\n--- Session Summary {conversation.created_at.date()} ---\n")
            f.write(summary)
        
        return JsonResponse({'status': 'success', 'summary': summary})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def generate_summary(messages):
    # Aquí puedes usar el mismo modelo de IA para generar un resumen
    # Por ahora, usaremos un resumen simple
    return "\n".join([f"{'User' if msg.is_user else 'AI'}: {msg.content[:50]}..." for msg in messages])

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        conversation_id = request.POST.get('conversation_id', None)

        if conversation_id:
            conversation = Conversation.objects.get(id=conversation_id)
        else:
            conversation = Conversation.objects.create()

        Message.objects.create(conversation=conversation, content=user_input, is_user=True)

        # Genera la respuesta del AI
        ai_response = generate_response(user_input, conversation)

        Message.objects.create(conversation=conversation, content=ai_response, is_user=False)

        return JsonResponse({
            'response': ai_response,
            'conversation_id': conversation.id
        })

def generate_response(prompt, conversation):
    conversation_history = Message.objects.filter(conversation=conversation).order_by('timestamp')
    context = "\n".join([f"{'User' if msg.is_user else 'AI'}: {msg.content}" for msg in conversation_history])

    full_prompt = f"Conversation history:\n{context}\n\nNew input: {prompt}"

    system_prompt = f"""You are an AI psychology assistant. Your task is to help users with psychological issues, provide support, and offer insights. The user's preferred language is {conversation.user_language}. Follow these guidelines:

    1. Communicate in the user's preferred language.
    2. Ask questions to understand the user's situation better.
    3. Provide empathetic and supportive responses.
    4. Offer practical advice and coping strategies when appropriate.
    5. Use psychological theories and concepts to explain behaviors and emotions.
    6. Suggest exercises or techniques that might help the user.
    7. Maintain a professional and ethical stance at all times.
    8. Encourage the user to seek professional help if their issues seem severe.

    Remember, your goal is to support and guide the user, not to replace professional psychological help."""

    try:
        output = replicate.run(
            "meta/meta-llama-3.1-405b-instruct",
            input={
                "prompt": full_prompt,
                "system_prompt": system_prompt,
                "max_tokens": 512,
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 50,
                "presence_penalty": 0,
                "frequency_penalty": 0
            }
        )

        if isinstance(output, list):
            output = "".join(output)

        return output
    except Exception as e:
        return f"Error generating response: {str(e)}"

@csrf_exempt
def speech_to_text(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        
        try:
            transcript = replicate.run(
                "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c",
                input={
                    "task": "transcribe",
                    "audio": audio_file,
                    "language": "None",
                    "timestamp": "chunk",
                    "batch_size": 64,
                    "diarise_audio": False
                }
            )

            transcribed_text = transcript['text'] if isinstance(transcript, dict) and 'text' in transcript else str(transcript)
            return JsonResponse({'text': transcribed_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        language = request.POST.get('language', 'en')
        
        try:
            audio_output = replicate.run(
                "lucataco/xtts-v2:684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e",
                input={
                    "text": text,
                    "speaker": "https://replicate.delivery/pbxt/JqzvJMqmYeWjdUSULrjJbEYjsYUnd335Keufr2QyMCGKJtY4/male.wav",
                    "language": language,
                    "cleanup_voice": False
                }
            )
            
            return JsonResponse({'audio_url': audio_output})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)