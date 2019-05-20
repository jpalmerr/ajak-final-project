(function() {
  var $ = function(id){return document.getElementById(id)};

  var canvas = this.__canvas = new fabric.Canvas('canvas', {
    isDrawingMode: true
  });

  canvas.freeDrawingBrush.width = 5;

  fabric.Object.prototype.transparentCorners = false;

  var clearEl = $('clear-canvas');

  clearEl.onclick = function() { canvas.clear() };

})();
