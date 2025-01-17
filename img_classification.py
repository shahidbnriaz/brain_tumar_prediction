from PIL import Image
from keras.preprocessing.image import load_img,img_to_array
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
def teachable_machine_classification(img, weights_file):
    
    model = keras.models.load_model(weights_file)

    
    data = np.ndarray(shape=(1, 384, 384, 3), dtype=np.float32)
    image = img
  
    size = (384, 384)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

  
    image_array = np.asarray(image)
  
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

  
    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)
