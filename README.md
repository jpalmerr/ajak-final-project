# Ajak Final Project

[![Build Status](https://travis-ci.com/jpalmerr/ajak-final-project.svg?branch=master)](https://travis-ci.com/jpalmerr/ajak-final-project)

This is our final project at Makers Academy, to be presented 24/5/19.

[Getting started](#getting-started) | [Project aims](#project-aims) | [Technologies](#technologies) | [Manifesto](#manifesto) | [Authors](#authors) | [Acknowledgements](#acknowledgements)

## Getting started

```bash
git clone https://github.com/jpalmerr/ajak-final-project
pip3 install -r requirements.txt # to install dependencies
```

```bash
npm install
```

### To download data

Download `Circle`, `Square` and `Triangle` from [Google QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap) and save to `/data` folder in the project.

### To train model

```bash
python3 lib/train.py
```

### To see model predict random image from test data

```bash
python3 lib/predict.py
```

### To run tests

The `pytest` framework is used for unit testing.

To run tests:     
`pytest`

To run test coverage:     
`pytest --cov=lib`

### To run linter

We are using a linter called `pylint` for this project.

To run the linter:    

`pylint [options] module_or_package`    
For example `pylint lib`

## Project aims

Our program aims to receive a user inputted shape from:
- circle
- square
- triangle

and our AI machine will return a prediction of the shape name.

## Technologies

- Python
- SKLearn library
- Keras API
- TensorFlow
- Google QuickDraw Dataset
- Travis CI
- Flask
- Fabric JS

## Manifesto

Our project [manifesto](https://github.com/jpalmerr/ajak-final-project/blob/master/manifesto.md).

Our [Trello board](https://trello.com/b/SAOvMM1v/ajak).

## Authors

[Alex Chen](https://github.com/alexanderchen6), [Amy Jordan](https://github.com/amyj0rdan), [James Palmer](https://github.com/jpalmerr), [Kim Diep](https://github.com/kimdiep).

## Acknowledgements

Makers Academy
