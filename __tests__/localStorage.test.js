const correctCounter = require("../static/js/localStorage")

xtest('correct counter returns number of correct attempts', () => {
  document.getElementById("percentageCorrect").innerHTML = ""
  expect(correctCounter().toBe(0))
})
