const chatroomPages = document.querySelectorAll('.history__chatroom-page');
const historyPages = document.querySelectorAll('.history__section--page');
var pageidAtual

function updateChatContentById(pageId) {

    $.ajax({
        url: 'get_chatroom_messages/',  
        data: { chatroomId: pageId },  // Enviar o ID do chatroom como parâmetro
        method: 'GET',
        success: function(data) {
            const chatBox = document.querySelector('.chat__box');
            const chatContent = document.createElement('div');

            // Adiciona as classes necessárias para o estilo do balão de mensagem
            chatContent.innerHTML = data;  // Insira aqui o HTML retornado pela requisição AJAX

            // Substitui o conteúdo da classe .chat__box pelo chatContent.innerHTML
            chatBox.innerHTML = chatContent.innerHTML;
        },
        error: function() {
            console.log('Erro ao obter as mensagens do chatroom.');
        }
    });
}

// Event listener para os elementos history__section--page
historyPages.forEach(page => {
    page.addEventListener('click', () => {
        const pageId = page.getAttribute('data-id');
        if (pageId) {
            pageidAtual = pageidAtual
            updateChatContentById(pageId);
        }
    });
});


function addMessageToChatroom() {
    const textarea = document.getElementById('question__input');
    const message = textarea.value.trim();

    if (message) {
        const chatroomId = pageidAtual;  

        // requisição AJAX para adicionar a mensagem ao chatroom correspondente
        $.ajax({
            url: '/add_message/',  // URL para adicionar a mensagem (necessário criar a view)
            data: { chatroomId: chatroomId, message: message },
            method: 'POST',
            success: function() {
                // Atualize o conteúdo do chat após adicionar a mensagem
                updateChatContentById(chatroomId);

                // Limpe o textarea após adicionar a mensagem
                textarea.value = '';
            },
            error: function() {
                console.log('Erro ao adicionar a mensagem ao chatroom.');
            }
        });
    }
}
