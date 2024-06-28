import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Load the trained CNN model
model = tf.keras.models.load_model('cnn_model.h5')

st.title("Brain Tumor Prediction App")

st.sidebar.header("Upload Brain MRI Image")

uploaded_file = st.sidebar.file_uploader("Upload an image file", type=["jpg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to the same size as the training images
    image = np.array(image)
    image = image / 255.0  # Normalize
    image = image.reshape(1, 28, 28, 1)  # Reshape for the model

    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Predict using the CNN model
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)

    st.subheader('Prediction')
    st.write('Tumor Detected' if predicted_class[0] == 1 else 'No Tumor')

    st.subheader('Prediction Probability')
    st.write(prediction)
else:
    st.write("Please upload an MRI image file.")
