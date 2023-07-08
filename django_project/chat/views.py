from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from chat.models import ChatRoom, Message
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from random import choice

# with open('static/motivational_quotes.txt', 'r') as file:
#     quotes = [line.strip() for line in file]

# def getQuote():
#     return choice(quotes)
def getQuote(message):
    return str(message)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='accounts:login')
def homePageView(request):
    user = request.user
    context = {}
    context['chatrooms'] = ChatRoom.objects.filter(user_id=user)
    context['hidechat'] = False
    context['settingdLogSectionItems'] = [["fa-solid fa-palette","Theme"],["fa-solid fa-trash-can","Clear data"],["fa-solid fa-file-export","Export data"]]
    context['limitations'] = ["May occasionally generate incorrect information","May occasionally produce harmful instructions or biased content", "Limited knowledge of world and events after 2021"]
    context['capabilities'] = ["Remenbers the inspirational quotessaid earlier in the conversation","Trained to decline any request","Help you to be aproved in an optative course"]
    context['examples'] = ['"Explain quantum computing in simple terms"', '"How to write a love song?"', '"What is the best programming language to building a chat like Whatsapp?"']
    return render(request, "home.html", context)

def get_chatroom_html(request):
    chatroom_id = request.GET.get('chatroomId')  # Obtém o ID do chatroom da requisição GET

    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        messages = Message.objects.filter(chat_room=chatroom)

        # Constrói o HTML com base nas mensagens
        html = ""
        for message in messages:
            if message.sender.is_superuser:
                html += f'<div class="message-admin" style="background-color: red;padding: 20px;margin:30px;border-radius:30px;word-wrap: break-word;">{message.message}<br><span style="font-size:10px">{message.timestamp}</span></div>'
            else:
                html += f'<div class="message-user" style="background-color: blue;padding: 20px;margin:30px;border-radius:30px;word-wrap: break-word;">{message.message}<br><span style="font-size:10px">{message.timestamp}</span></div>'
        return HttpResponse(html, content_type='text/html')
    except ChatRoom.DoesNotExist:
        return HttpResponseBadRequest("Chatroom não encontrado.")
    

    from django.http import HttpResponseBadRequest

@csrf_exempt  # Para desabilitar a verificação de token CSRF
def add_message(request):
    if request.method == 'POST':
        chatroom_id = request.POST.get('chatroomId')
        message = request.POST.get('message')

        try:
            chatroom = ChatRoom.objects.get(id=chatroom_id)
            sender = request.user  # Obtém o usuário logado
            print(sender)

            # user message
            message = Message(chat_room=chatroom, sender=sender, message=message)
            message.save()

            # chat message
            message = Message(chat_room=chatroom, sender=User.objects.get(username="admin", is_superuser=True), message="message[0]")
            message.save()
            
            return HttpResponse(status=200)  # Resposta de sucesso
        except ChatRoom.DoesNotExist:
            return HttpResponseBadRequest("Chatroom não encontrado.")
    
    return HttpResponseBadRequest("Requisição inválida.")
