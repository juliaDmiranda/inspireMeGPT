from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from chat.models import ChatRoom, Message
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import requests
import json
from django.utils import timezone
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='accounts:login')
def homePageView(request):
    user = request.user
    
    context = {}
    context['chatrooms'] = ChatRoom.objects.filter(user_id=user)
    context['user'] = user
    context['settingdLogSectionItems'] = [["fa-solid fa-palette","Theme"],["fa-solid fa-trash-can","Clear data"],["fa-solid fa-file-export","Export data"]]
    context['limitations'] = ["May occasionally generate incorrect information","May occasionally produce harmful instructions or biased content", "Limited knowledge of world and events after 2021"]
    context['capabilities'] = ["Remenbers the inspirational quotessaid earlier in the conversation","Trained to decline any request","Help you to be aproved in an optative course"]
    context['examples'] = ['"Explain quantum computing in simple terms"', '"How to write a love song?"', '"What is the best programming language to building a chat like Whatsapp?"']
    
    return render(request, "home.html", context)

def get_chatroom_html(request):
    chatroom_id = request.GET.get('chatroomId')
    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        messages = Message.objects.filter(chat_room=chatroom)
        context = {'messages':messages}
        return render(request, 'chat.html', context)
    except ChatRoom.DoesNotExist:
        return HttpResponseBadRequest("Chatroom não encontrado.")
    
@csrf_exempt  # desable token CSRF verification (why?)
def add_message(request):
    user = request.user
    if request.method == 'POST' or request.method == 'GET':
        if(request.method == 'GET'):
            chatroom_id = request.GET.get('chatroomId')
            message = request.GET.get('message')
        else:    
            chatroom_id = request.POST.get('chatroomId')
            message = request.POST.get('message')
        try:
            chatroom = ChatRoom.objects.get(id=chatroom_id)
            sender = request.user
            chatroom.timestamp = timezone.now()
            # user message
            message = Message(chat_room=chatroom, sender=sender, message=message)
            message.save()

            # chat message
            inspirationaQuote = requests.get("https://zenquotes.io/api/random/").json()[0]
            quote =  f'" {inspirationaQuote["q"]} " ({inspirationaQuote["a"]})'
            message = Message(chat_room=chatroom, sender=User.objects.get(username="admin", is_superuser=True), message=quote)
            message.save()

            context = {'chatrooms': ChatRoom.objects.filter(user_id=user)}

            html = render(request, 'chatrooms.html', context).content.decode('utf-8') # rendered html to string

            return HttpResponse(json.dumps({'id':chatroom_id, 'html':html, 'author':inspirationaQuote['a']}), content_type='application/json', status=200)  # Resposta de sucesso
        except ChatRoom.DoesNotExist:
            return HttpResponseBadRequest("Chatroom não encontrado.")
    
    return HttpResponseBadRequest("Requisição inválida.")

@csrf_exempt  # desable token CSRF verification
def create_chatroom(request):
    try:
        latest_id = ChatRoom.objects.latest('id').id
    except ChatRoom.DoesNotExist:
        latest_id = 0
    user = request.user
    chatroom = ChatRoom(title=f"Chat Room {latest_id+1}", user_id=user)
    chatroom.save()
    message = request.POST.get('message')
    return redirect(reverse('chat:add_message') + f'?chatroomId={chatroom.id}&message={message}')