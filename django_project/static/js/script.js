// window.onload = function() {
//             //     var questionInput = document.querySelector(".question__input__input");
            
//             //     questionInput.value = "";
            // };

function exampleToInputEvent(event) {
    var questionInput = document.querySelector(".question__input__input");
    questionInput.value = event.target.textContent.substring(1, event.target.textContent.length - 1);
}

function newChat(){
    $('.chatContentContainer').prop('hidden', true);
    $('.chatgpt__title').prop('hidden', false);
    // $('.box__examples__capabilities__limitations').prop('hidden', false);
    $('.examples').prop('hidden', false);
    $('.capabilities').prop('hidden', false);
    $('.limitations').prop('hidden', false);
    chatroom_id_current = -1
}

function updateChatContentById(event,chatroom_id) {
    if(chatroom_id_current==-1 && chatroom_id ==-1){
        addMessageToChatroom(event)
    }
    else{
        chatroom_id_current = chatroom_id
        $.ajax({
            url: 'get_chatroom_messages/',  // URL para buscar as mensagens do chatroom (necessário criar a view)
            data: { chatroomId: chatroom_id },  // Enviar o ID do chatroom como parâmetro
            method: 'GET',
            success: function(data) {
                
                chatContent.innerHTML = data;
                chatBox.appendChild(chatContent);

                $('.chatgpt__title').prop('hidden', true);
                $('.examples').prop('hidden', true);
                $('.capabilities').prop('hidden', true);
                $('.limitations').prop('hidden', true);
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
        // Faça uma requisição AJAX para adicionar a mensagem ao chatroom correspondente
        console.log(chatroom_id_current)
        if(chatroom_id_current ==  -1){
            url = 'create_chatroom/'
            data = {message:questionInput.value}
        }
        else {
            url = 'add_message/'
            data = { chatroomId: chatroom_id_current, message:questionInput.value}
        }
        
        $.ajax({
            url: url,  // URL para adicionar a mensagem (necessário criar a view)
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