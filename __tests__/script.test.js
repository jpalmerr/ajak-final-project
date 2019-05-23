jest.mock('../static/js/script')

test('clicks predictButton and ajax request is sent', () => {

  document.body.innerHTML =
  '<div>' +
  ' <span id="result"></span>' +
  ' <button id="predictButton">Predict</button>' +
  '</div>';

  const $ = require('jquery')
  require('../static/js/script')

  $('#predictButton').click();

  expect($('#result').text()).toEqual('Prediction Output: ')
})
