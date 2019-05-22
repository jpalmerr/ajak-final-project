$("#predictButton").click(function(event){
  event.preventDefault()
  var canvasObj = document.getElementById("canvas");
  var img = canvasObj.toDataURL();
  $.ajax({
    type: "POST",
    url: $SCRIPT_ROOT + "/predict/",
    data: img,
    success: function(data){
      $('#result').text(' Predicted Output: '+data);
    }
  });
});

function correctCounter() {

    if (localStorage.clickcount) {
      localStorage.clickcount = Number(localStorage.clickcount)+1;
      localStorage.correctAttempts = Number(localStorage.correctAttempts)+1 
    } else {
      localStorage.clickcount = 1;
      localStorage.correctAttempts = 1 
    }
    percentageTracker()
}

function incorrectCounter() {
  if (localStorage.clickcount) {
    localStorage.clickcount = Number(localStorage.clickcount)+1;
  } else {
    localStorage.clickcount = 1;
    localStorage.correctAttempts = 0
  }
  percentageTracker()
}

function percentageTracker(){
  var totalAttempts = localStorage.clickcount
  var percentage = (localStorage.correctAttempts / totalAttempts) * 100
  document.getElementById("percentageCorrect").innerHTML = Math.round(percentage)
}

$("#playAgain").click(function(event){
  localStorage.clear();
  document.getElementById("percentageCorrect").innerHTML = ""
})
