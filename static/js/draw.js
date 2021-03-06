(function(exports) {
  var $ = function(id){return document.getElementById(id)};

  var canvas = this.__canvas = new fabric.Canvas('canvas', {
    isDrawingMode: true
  });

  canvas.freeDrawingBrush.width = 5;

  fabric.Object.prototype.transparentCorners = false;

  var clearEl = $('clear-canvas');

  var n = 0;
  var predictButtonClicked = false;

  clearEl.onclick = function() {
    canvas.clear()
    document.getElementById('result').innerHTML = ""
    if (predictButtonClicked === true) {
      n = 0
      predictButtonClicked = false
      document.getElementById('timer').innerHTML = 20
    }
  };

  canvas.on('mouse:down', function() {
    if (n === 0) {
      var timeLeft = 19;
      var timer = document.getElementById('timer');
      var predictButton = document.getElementById('predict-button')

      var timerId = setInterval(countdown, 1000);

      function countdown() {
        if (timeLeft < 0) {
          clearTimeout(timerId);
          predictButton.click();
        } else if (predictButtonClicked === true) {
          clearTimeout(timerId);
          timer.innerHTML = timeLeft;
        } else {
          timer.innerHTML = timeLeft;
          timeLeft--;
        }
      }
    }
    n += 1
  });

  function stopCountdown() {
    predictButtonClicked = true
  }
  exports.stopCountdown = stopCountdown;
})(this);
