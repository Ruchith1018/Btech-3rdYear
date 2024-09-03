# Sarcasm Detection using BERT and GCN

This project focuses on detecting sarcasm in text using a combination of BERT (Bidirectional Encoder Representations from Transformers) and GCN (Graph Convolutional Networks). The model is designed to accurately identify sarcastic remarks in social media posts, reviews, and other text data.

## Table of Contents

- [Introduction](#introduction)
- [Approach](#approach)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Sarcasm is a complex form of expression that is often challenging to detect using traditional natural language processing techniques. This project leverages advanced models like BERT for contextual understanding and GCN for capturing relationships between words to improve sarcasm detection in text.

## Approach

- **BERT:** Pre-trained BERT is used to capture the contextual meaning of words in a sentence, which is crucial for understanding sarcasm.
- **GCN:** A Graph Convolutional Network is applied to model the relationships between words in the text, further enhancing the detection accuracy.

## Technologies Used

- Python
- PyTorch or TensorFlow (for BERT and GCN implementation)
- Hugging Face Transformers
- NetworkX (for graph creation and manipulation)
- Scikit-learn
- Pandas
- NumPy
- Jupyter Notebook

## Usage

1. **Data Preprocessing:**
   - Load the text data and preprocess it by tokenizing and creating word embeddings using BERT.
   - Construct graphs representing the relationships between words in the text.

2. **Model Training:**
   - Train the GCN model on top of the BERT embeddings to classify text as sarcastic or non-sarcastic.

3. **Evaluation:**
   - Evaluate the model using metrics like accuracy, precision, recall, and F1-score.

4. **Prediction:**
   - Use the trained model to detect sarcasm in new text inputs.


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.


## Acknowledgements

- The project was inspired by recent advancements in NLP, particularly in sarcasm detection using deep learning models.
- Special thanks to the developers of Hugging Face, PyTorch, TensorFlow, and other open-source tools used in this project.
- The dataset used for training and testing was obtained from kaggle.


