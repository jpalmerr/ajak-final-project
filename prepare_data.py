import numpy as np

def load(dir, files):
    "returning list of numpy arrays"

    data = []
    for file in files:
        f = np.load(dir + file)

        for i in range(len(f)):
            x = np.reshape(f[i], (28, 28))
            x = np.expand_dims(x, axis=0)
            x = np.reshape(f[i], (28, 28, 1))
            data.append(x)

    return data

def normalize(data):
    "returns normalized form"

    return np.interp(data, [0, 255], [-1,1])

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

# data = load('data/', ['circles.npy'])
# normalize(data)
# print(set_limit([[0,1,2,3,4,5,6,7,8,9]], 2))
# print(generate_labels(5, 4))
