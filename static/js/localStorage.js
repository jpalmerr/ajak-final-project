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
  document.getElementById("percentage-correct").innerHTML = `Correctly guessed: ${Math.round(percentage)}%`
}
