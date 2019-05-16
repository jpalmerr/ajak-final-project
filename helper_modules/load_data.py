from sklearn.model_selection import train_test_split as tts
from prepare_data import *
from constants import *

FILES = ["circles.npy", "squares.npy", "triangles.npy"]

shapes = load("data/", FILES, True)

shapes = set_limit(shapes, N_SAMPLES)

shapes = list(map(normalize, shapes))

labels = generate_labels(N_SHAPES, N_SAMPLES)

x_train, x_test, y_train, y_test = tts(shapes, labels, test_size=0.10)
