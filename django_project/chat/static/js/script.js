function exampleToInputEvent(event) {
    var questionInput = document.querySelector(".question__input__input");
    questionInput.value = event.target.textContent.substring(1, event.target.textContent.length - 1);
}

function newChat(){
    $('.chatContentContainer').prop('hidden', true);
    // $('.chatgpt__title').prop('hidden', false);
    // $('.examples').prop('hidden', false);
    // $('.capabilities').prop('hidden', false);
    // $('.limitations').prop('hidden', false);
    $('.tohide').prop('hidden', false);

    
    chatroom_id_current = -1
}

function updateChatContentById(event,chatroom_id) {
    if(chatroom_id_current==-1 && chatroom_id ==-1){
        addMessageToChatroom(event)
    }
    else{
        chatroom_id_current = chatroom_id
        $.ajax({
            url: 'get_chatroom_messages/', 
            data: { chatroomId: chatroom_id },
            method: 'GET',
            success: function(data) {
                
                chatContent.innerHTML = data;
                chatBox.appendChild(chatContent);
                $('.tohide').prop('hidden', true);
                // $('.chatgpt__title').prop('hidden', true);
                // $('.examples').prop('hidden', true);
                // $('.capabilities').prop('hidden', true);
                // $('.limitations').prop('hidden', true);
                $('.chatContentContainer').prop('hidden', false);
            },
            error: function(data) {
                console.log("Error on updateChatContentById");
                console.log(data)
            }
        });
    }
}

function addMessageToChatroom(event) {
    if(questionInput.value ==''){
        console.log("STRING VAZIA")
    }
    else {
        let url
        let data
        
        if(chatroom_id_current ==  -1){
            url = 'create_chatroom/'
            data = {message:questionInput.value}
        }
        else {
            url = 'add_message/'
            data = { chatroomId: chatroom_id_current, message:questionInput.value}
        }
        
        // AJAX request
        $.ajax({
            url: url,
            data: data,
            method: 'POST',
            success: function(data) {
                chatroom_id_current = data.id
                console.log("CURRENTLY")
                console.log(data)
                
                historyContent.innerHTML = data.html;

                updateChatContentById(event, chatroom_id_current);
                questionInput.value = '';
            },
            error: function(data) {
                console.log(url)
                console.log("addMessage didn't work");
            }
            });
    }
}