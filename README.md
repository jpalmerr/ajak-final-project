# Ajak Final Project

[![Build Status](https://travis-ci.com/jpalmerr/ajak-final-project.svg?branch=master)](https://travis-ci.com/jpalmerr/ajak-final-project)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)



This is our final project at Makers Academy, to be presented 24/5/19.

Visit our web app, [Ajak Doodler](https://ajak-doodler.herokuapp.com/)!

[Getting started](#getting-started) | [Project aims](#project-aims) | [Technologies](#technologies) | [Manifesto](#manifesto) | [Authors](#authors) | [Acknowledgements](#acknowledgements)

## Getting started

```bash
git clone https://github.com/jpalmerr/ajak-final-project
pip3 install -r requirements.txt # to install python dependencies
npm install # to install node dependencies
```

### To download data

Download `Crown`, `Camera` and `Rabbit` from [Google QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap) and save to `/data` folder in the project under `crowns.npy`, `cameras.npy` and `rabbits.npy`.

### To train model

```bash
python3 model_config/train.py
```

When prompted by running the above command, save the model as `cameras_rabbits_crowns_model`

### To see model predict random image from test data

```bash
python3 model_config/predict_on_command_line.py
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

Our program aims to receive a user's drawing of a:
- crown
- camera
- rabbit

and our AI machine will return a prediction of the drawing.

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
