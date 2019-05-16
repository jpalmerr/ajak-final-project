import sys
sys.path.append('./helper_modules')
from prepare_data import *
from sklearn.model_selection import train_test_split as tts
from keras.utils import np_utils
from conv import conv
from random import randint
from constants import *
from load_data import *

Y_train = np_utils.to_categorical(y_train, N_SHAPES)
Y_test = np_utils.to_categorical(y_test, N_SHAPES)

model = conv(classes=N_SHAPES, input_shape=(28, 28, 1))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

input("1, 2, 3... enter 4 to start training: ")
print("Starting training")

model.fit(np.array(x_train), np.array(Y_train), batch_size=32, epochs=N_EPOCHS, verbose=1)

print("Training over")

print("Running predictions")
preds = model.predict(np.array(x_test))

count = 0
for i in range(len(preds)):
    if np.argmax(preds[i]) == y_test[i]:
        count += 1

print("Accuracy: ", ((count + 0.0) / len(preds)) * 100)

name = input("Enter name to save trained model: ")
model.save(name + ".h5")
print("Model saved")
