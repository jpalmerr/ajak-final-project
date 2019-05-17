# Ajak Final Project

[![Build Status](https://travis-ci.com/jpalmerr/ajak-final-project.svg?branch=master)](https://travis-ci.com/jpalmerr/ajak-final-project)

This is our final project at Makers Academy, to be presented 24/5/19.

## Getting started

```bash
git clone https://github.com/jpalmerr/ajak-final-project
pip3 install -r requirements.txt # to install dependencies
```

## To download data

Download `Circle`, `Square` and `Triangle` from [Google QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap) and save to `/data` folder in the project.

## To train model

```bash
python3 lib/train.py
```

## To see model predict random image from test data

```bash
python3 lib/predict.py
```

## Project Name

Our program aims to receive a user inputted shape from:
- circle
- square
- triangle

and our AI machine will return the correct shape name.

## Performance Results

To run test coverage:
`pytest --cov=lib`

## Technologies

- Python
- SKLearn library
- Keras API
- TensorFlow
- Google Quick Draw Dataset
- Travis

## Manifesto

Our project [manifesto](https://github.com/jpalmerr/ajak-final-project/blob/master/manifesto.md).

Our [Trello board](https://trello.com/b/SAOvMM1v/ajak).

## Authors

Alex Chen, Amy Jordan, James Palmer, Kim Diep.

## Acknowledgements

Makers Academy
