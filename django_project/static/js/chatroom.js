// Event listener para os elementos history__chatroom-page
const chatroomPages = document.querySelectorAll('.history__chatroom-page');

const historyPages = document.querySelectorAll('.history__section--page');

var pageidAtual 
// chatroomPages.forEach(page => {
//     page.addEventListener('click', () => {
//         // const pageId = page.getAttribute('data-id');
//         if (pageId) {
//             // Fazer uma requisição AJAX para buscar o HTML do chatroom com o ID correspondente
//             $.ajax({
//                 url: '/get_chatroom_html/',  // URL para buscar o HTML do chatroom (necessário criar a view)
//                 data: { chatroomId: pageId },  // Enviar o ID do chatroom como parâmetro
//                 method: 'GET',
//                 success: function(data) {
//                     // Atualizar o conteúdo da página com o HTML retornado pela requisição AJAX
//                     const chatContent = document.getElementById('chatContentContainer');
//                     chatContent.innerHTML = data;
//                 },
//                 error: function() {
//                     console.log('Erro ao obter o HTML do chatroom.');
//                 }
//             });
//         }
//     });
// });

// Função para atualizar o conteúdo da classe .chat__box com base no ID do history__section--page
function updateChatContentById(pageId) {
    // Fazer uma requisição AJAX ou usar o seu backend para buscar as mensagens do chatroom com o ID correspondente
    // Exemplo de requisição AJAX usando jQuery
    $.ajax({
        url: 'get_chatroom_messages/',  // URL para buscar as mensagens do chatroom (necessário criar a view)
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
        const chatroomId = pageidAtual;  // Obtenha o ID do chatroom atual

        // Faça uma requisição AJAX para adicionar a mensagem ao chatroom correspondente
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
