const BASE_URL = "http://localhost:5000/";
const $wordGuessFormButton = $("#word-guess-button");
const $wordGuessInput = $("#word-guess-input");
const $messageArea = $("#message-area");

$wordGuessFormButton.on("click", async function(event){
  event.preventDefault();

  let guessInputValue = $wordGuessInput.val();
  response = await axios.post(BASE_URL + "check/",{
    "guess":guessInputValue});

    console.log("This is the response from our server", response)

    returnMessage(response.data);
  });
  

function returnMessage(response) {
  
  $messageArea.text(response);


}