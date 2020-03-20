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
    let scoreOfGuess = calcScore(response.data,guessInputValue);
    
    appendScore(scoreOfGuess);
    
  });
  

function returnMessage(response) {
  
  $messageArea.text(response);


}

function calcScore(response,guess) {
  let score = 0
  if(response === "Cool! Good job Guy") {
    score = guess.length
   
  }
  return score; 
}

function appendScore(score) {
  let currentScore = Number($("#score").text());
  let newScore = Number(score);
  let scoreToAppend = String(newScore + currentScore);
  $("#score").text(scoreToAppend);
}