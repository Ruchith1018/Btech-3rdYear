##### PREPARATIONS

# libraries
import gc
import os
import pickle
import sys
import urllib.request
import requests
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# custom libraries
sys.path.append('code')
from model import get_model
from tokenizer import get_tokenizer

# download with progress bar
mybar = None
def show_progress(block_num, block_size, total_size):
    global mybar
    if mybar is None:
        mybar = st.progress(0.0)
    downloaded = block_num * block_size / total_size
    if downloaded <= 1.0:
        mybar.progress(downloaded)
    else:
        mybar.progress(1.0)
        
        
##### CONFIG

# page config
st.set_page_config(page_title            = "Readability prediction", 
                   page_icon             = ":books:", 
                   layout                = "centered", 
                   initial_sidebar_state = "collapsed", 
                   menu_items            = None)


##### HEADER

# title
st.title('Text readability prediction')


st.write('This app uses deep learning to estimate the reading complexity of a custom text. Enter your text below, and we will run it through one of the two transfomer models and display the result.')


##### PARAMETERS

# title
st.header('How readable is your text?')

# model selection
model_name = st.selectbox(
    'Which model would you like to use?',
    ['DistilBERT'])

# input text
input_text = st.text_area('Which text would you like to rate?', 'Please enter the text in this field.')


##### MODELING

# compute readability
if st.button('Compute readability'):

    # specify paths
    if model_name == 'DistilBERT':
        folder_path = 'output/v59/'
        weight_path = 'https://github.com/kozodoi/Kaggle_Readability/releases/download/0e96d53/weights_v59.pth'


    # download model weights
    if not os.path.isfile(folder_path + 'pytorch_model.bin'):
        with st.spinner('Downloading model weights. This is done once and can take a minute...'):
            urllib.request.urlretrieve(weight_path, folder_path + 'pytorch_model.bin', show_progress)

    # compute predictions
    with st.spinner('Computing prediction...'):

        # clear memory
        gc.collect()

        # load config
        config = pickle.load(open(folder_path + 'configuration.pkl', 'rb'))
        config['backbone'] = folder_path

        # initialize model
        model = get_model(config, name = model_name.lower(), pretrained = folder_path + 'pytorch_model.bin')
        model.eval()

        # load tokenizer
        tokenizer = get_tokenizer(config)

        # tokenize text
        text = tokenizer(text                  = input_text,
                         truncation            = True,
                         add_special_tokens    = True,
                         max_length            = config['max_len'],
                         padding               = False,
                         return_token_type_ids = True,
                         return_attention_mask = True,
                         return_tensors        = 'pt')
        inputs, masks, token_type_ids = text['input_ids'], text['attention_mask'], text['token_type_ids']

        # clear memory
        del tokenizer, text, config
        gc.collect()

        # compute prediction
        if input_text != '':
            prediction = model(inputs, masks, token_type_ids)
            prediction = prediction['logits'].detach().numpy()[0][0]
            prediction = 100 * (prediction + 4) / 6 # scale to [0,100]

        # clear memory
        del model, inputs, masks, token_type_ids
        gc.collect()

        # print output
        st.metric('Readability score:', '{:.2f}%'.format(prediction, 2))
        st.write('**Note:** readability scores are scaled to [0, 100%]. A higher score means that the text is easier to read.')
        st.success('Success! Thanks for scoring your text :)')

