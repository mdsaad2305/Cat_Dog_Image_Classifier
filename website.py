import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import load_model
import os

st.header("Cat and Dog Image Classification")

st.write("This model gives out 2 results: -")
st.markdown("- Whether the image is a cat or a dog")
st.markdown("- The score of the image. Score < 0.5 indicates a cat and score > 0.5 indicates a dog")

def main():
    upload = st.file_uploader("Choose a cat/dog image (jpg files only)", type='jpg')
    if upload is not None:
        image = Image.open(upload)
        animal = plt.figure()
        plt.imshow(image)
        st.pyplot(animal)
        if st.button("Predict"):
            #plt.axis('off')
            predict_image(image)
            st.write("To predict another image, upload another image above.")

def predict_image(image):
    classifier = load_model(os.path.join('models', 'cat_dog_classifier.h5'))
    pred_image = tf.image.resize(image, (200,200))
    animal_pred = classifier.predict(np.expand_dims(pred_image/255, 0))
    if animal_pred[0][0] < 0.5:
        st.write("It is a Cat\n")
        st.write("Score = ",animal_pred[0][0])
    else:
        st.write("It is a Dog\n")
        st.write("Score = ",animal_pred[0][0])    


if __name__ == "__main__":
    main()
