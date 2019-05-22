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
    } else {
      localStorage.clickcount = 1;
    }
    document.getElementById("totalAttempts").innerHTML = localStorage.clickcount;
    document.getElementById("correctAttempts").innerHTML = localStorage.clickcount;
    percentageTracker()
}

function incorrectCounter() {
  if (localStorage.clickcount) {
    localStorage.clickcount = Number(localStorage.clickcount)+1;
  } else {
    localStorage.clickcount = 1;
  }
  document.getElementById("totalAttempts").innerHTML = localStorage.clickcount;
  percentageTracker()

}

function percentageTracker(){
  var totalAttempts= parseInt(document.getElementById('totalAttempts').innerHTML)
  var correctAttempts = parseInt(document.getElementById('correctAttempts').innerHTML)
  var percentage = (correctAttempts / totalAttempts) * 100 
  document.getElementById("percentageCorrect").innerHTML = Math.round(percentage)

}








// $("#correctPrediction").click(function(event){
//   event.preventDefault()

//   var n = localStorage.getItem('totalAttempts')

// // create localstorage

//   console.log(n)

//   if (n === null) {

//     n = 0;
//   }
//   n++

//   localStorage.setItem('totalAttempts', n);

//   document.getElementById('totalAttempts').innerHTML = n

// increase count
// })
