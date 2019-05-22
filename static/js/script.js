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

var correctAttempts = 0

function correctCounter() {

    if (localStorage.clickcount) {
      localStorage.clickcount = Number(localStorage.clickcount)+1;
      correctAttempts += 1
    } else {
      localStorage.clickcount = 1;
      correctAttempts += 1
    }
    percentageTracker()
}

function incorrectCounter() {
  if (localStorage.clickcount) {
    localStorage.clickcount = Number(localStorage.clickcount)+1;
  } else {
    localStorage.clickcount = 1;
  }
  percentageTracker()
}

function percentageTracker(){
  var totalAttempts = localStorage.clickcount
  var percentage = (correctAttempts / totalAttempts) * 100
  document.getElementById("percentageCorrect").innerHTML = Math.round(percentage)
}

$("#playAgain").click(function(event){
  localStorage.clear();
  correctAttempts = 0
  document.getElementById("percentageCorrect").innerHTML = 0
})
