$("#predict-button").click(function(event){
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

$("#reset-score").click(function(event){
  localStorage.clear();
  document.getElementById("percentage-correct").innerHTML = ""
})
