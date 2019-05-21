from flask import Flask, render_template, request
import sys
from PIL import Image
sys.path.append('./lib')
from drawing import *
from prediction import *
import base64
import re
from keras import backend as K

app = Flask(__name__)

# decoding an image from base64 into raw representation
def convertImage(imgData1):
    imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict/', methods=['GET', 'POST'])
def predict():

    image = request.get_data()
    image = convertImage(image)
    image = Image.open("output.png")
    new_image = Image.new("RGBA", (280, 280), "WHITE")
    new_image.paste(image, (0, 0), image)
    new_image.convert('RGBA').save('output.png')
    drawing = Drawing(new_image)
    drawing = drawing.reshape()
    prediction = Prediction(drawing)
    predictionNow = prediction.predict()
    K.clear_session()
    return predictionNow

if __name__ == "__main__":
    app.run(debug=True)
