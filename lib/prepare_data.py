import numpy as np

def load(directory, files, reshaped):
    "returning list of numpy arrays"

    data = []
    for file in files:
        f = np.load(directory + file)
        if reshaped:
            new_f = []
            for i in range(len(f)):
                x = np.reshape(f[i], (28, 28))
                x = np.expand_dims(x, axis=0)
                x = np.reshape(f[i], (28, 28, 1))
                new_f.append(x)
            f = new_f
        data.append(f)
    return data

def normalize(data):
    "returns normalized form"

    return np.interp(data, [0, 255], [-1, 1])

def set_limit(arrays, n):
    "Limit to n elements and return a single list"
    limited_list = []
    for array in arrays:
        i = 0
        for item in array:
            if i == n:
                break
            limited_list.append(item)
            i += 1
    return limited_list

def generate_labels(classes, samples):
    "generate labels from 0 to no. of classes, repeated for each sample"
    labels = []
    for i in range(classes):
        labels += [i] * samples
    return labels
