// // Retrieve all elements with class "examples__lil__box"
// let exampleBoxes = document.getElementsByClassName("examples__lil__box");
            
// function exampleToInputEvent(event) {
//     var questionInput = document.querySelector(".question__input__input");
    
//     questionInput.value = event.target.textContent.substring(1, event.target.textContent.length - 1);
// }

// for (var i = 0; i < exampleBoxes.length; i++) {
//     exampleBoxes[i].addEventListener("click", exampleToInputEvent);
// }


// let question__input = document.getElementById("question__input-event");
//             let examples = document.querySelectorAll(".examples__lil__box");
            
//             function messager__4__users__event(){
//             var newImage = document.createElement("img");
//             newImage.src = "../static/img/stonks.png";
//             newImage.className = "stonks__img";

//             var newDiv = document.createElement("div");
//             newDiv.className = "messager__4__users--text";
//             newDiv.innerHTML = "To be honest with you, anything you ask, I'll give you an inspirational quote. Look on the bright side, you might not learn about quantum computing, but you'll feel inspired enough to do it yourself.";

//             var quitButton = document.createElement('i');
//             quitButton.className = "fa-regular fa-circle-xmark";
//             quitButton.id = "quit"
//             quitButton.addEventListener('mouseover', function() {
//                 this.style.cursor = "pointer";
//             });

//             var myDiv = document.getElementById("my-div");
//             myDiv.appendChild(newImage);
//             myDiv.appendChild(newDiv);
//             myDiv.appendChild(quitButton);
//             myDiv.classList.add("page-opening"); // Add the page-opening class

//             var element = document.querySelector("#my-div");
//             element.style.backgroundColor = "white";
//             element.style.boxShadow = "0px 10px 30px white";

//             question__input.removeEventListener("click", messager__4__users__event);
//             examples.forEach(function (example) {
//             example.removeEventListener("click", messager__4__users__event);
//             });
//             }
//             question__input.addEventListener("click", messager__4__users__event);
            
//             examples.forEach(function(example) {
//                 example.addEventListener("click", messager__4__users__event);
//             });
            
            
//             document.addEventListener("click", function (event) {
//             if (event.target.id === "quit") {
//                 var myDiv = document.getElementById("my-div");
//                 myDiv.style.display = "none";
//             }
//             });

window.onload = function() {
    var questionInput = document.querySelector(".question__input__input");

    questionInput.value = "";
};