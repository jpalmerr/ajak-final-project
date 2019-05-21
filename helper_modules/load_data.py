from sklearn.model_selection import train_test_split as tts
from constants import *
import sys
sys.path.append('./lib')
from prepare_data import *

FILES = ["circles.npy", "squares.npy", "triangles.npy"]

items = load("data/", FILES, True)

items = set_limit(items, N_SAMPLES)

items = list(map(normalize, items))

labels = generate_labels(N_ITEMS, N_SAMPLES)

x_train, x_test, y_train, y_test = tts(items, labels, test_size=0.10)
