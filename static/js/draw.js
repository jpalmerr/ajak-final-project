(function() {
  var $ = function(id){return document.getElementById(id)};

  var canvas = this.__canvas = new fabric.Canvas('canvas', {
    isDrawingMode: true
  });

  canvas.freeDrawingBrush.width = 5;

  fabric.Object.prototype.transparentCorners = false;

  var clearEl = $('clear-canvas');

  clearEl.onclick = function() {
    canvas.clear()
    document.getElementById('result').innerHTML = ""
  };

  var timeLeft = 30;
  var element = document.getElementById('timer');

  var timerId = setInterval(countdown, 1000);

  function countdown() {
    if (timeLeft == 0) {
      clearTimeout(timerId);
      document.getElementById('predictButton').click();
    } else {
      element.innerHTML = timeLeft;
      timeLeft--;
    }
  }

})();
