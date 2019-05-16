import base64
from PIL import Image

class Drawing():
  def __init__(self, png):
    self.png = png
    
  def resize(self):
    return (self.png).resize((28, 28))