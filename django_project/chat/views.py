from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='accounts:login')
def homePageView(request):
    return render(request, "home.html")

# @csrf_exempt
# def create_message(request):
#     if request.method == "POST":
#         # Get the sender, chat_room, and message data from the request
#         sender_id = request.POST.get("sender")
#         chat_room_id = request.POST.get("chat_room")
#         message_text = request.POST.get("message")

#         try:
#             # Get the sender and chat_room objects
#             sender = User.objects.get(id=sender_id)
#             chat_room = ChatRoom.objects.get(id=chat_room_id)

#             # Create the new message
#             message = Message.objects.create(chat_room=chat_room, sender=sender, message=message_text)

#             # Return a JSON response indicating success
#             return JsonResponse({"message": "Message created successfully."})
#         except (User.DoesNotExist, ChatRoom.DoesNotExist):
#             # Handle any errors
#             return JsonResponse({"error": "Invalid sender or chat room."}, status=400)

#     # Return a JSON response indicating failure
#     return JsonResponse({"error": "Invalid request method."}, status=400)
