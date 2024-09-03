# Tomato Leaf Disease Detection using Deep Learning

This project aims to detect diseases in tomato leaves using deep learning techniques. The goal is to accurately classify tomato leaf images into different disease categories, thereby aiding in early detection and management of plant health.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Tomato plants are susceptible to various diseases that can affect crop yield and quality. Early and accurate detection of these diseases is essential for effective treatment. This project utilizes a Convolutional Neural Network (CNN) to classify images of tomato leaves into different disease categories.

## Dataset

- The dataset used in this project consists of images of tomato leaves, categorized into healthy and various disease-affected groups.

## Model Architecture

- The model is based on a Convolutional Neural Network (CNN) architecture, which is well-suited for image classification tasks.
- The architecture includes multiple convolutional layers followed by pooling layers, and fully connected layers leading to the final classification output.

## Technologies Used

- Python
- TensorFlow/Keras
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook

## Usage
Load the dataset and preprocess the images (resizing, normalization, etc.).
Train the CNN model using the training data.
Evaluate the model on the test data and fine-tune it if necessary.
Use the trained model to predict the disease category of new tomato leaf images.

## Acknowledgements
The dataset was sourced from kaggle.
This project was inspired by various research papers and online tutorials on plant disease detection using deep learning.
Special thanks to the contributors of TensorFlow/Keras and other open-source libraries used in this project.
