import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle

st.title('Next word prediction')

model = load_model('nextword1.h5')
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

def Predict_Next_Words(model, tokenizer, text):
        sequence = tokenizer.texts_to_sequences([text])[0]
        sequence = np.array(sequence)
        
        preds = model.predict_classes(sequence)

        predicted_word = ""
        
        for key, value in tokenizer.word_index.items():
            if value == preds:
                predicted_word = key
                break
        
        print(predicted_word)
        return predicted_word
        st.write(predicted_word)


text = st.text_input('enter the line',key=1)
    
if st.button('Predict',key=2):
    
    def tryy():
        try:
            text = st.text_input('enter the line')
            text = text.split(" ")
            text = text[-1]
            text = ''.join(text)
            an=Predict_Next_Words(model, tokenizer, text)
            st.text(an)
        except:
                tryy();
    tryy();


