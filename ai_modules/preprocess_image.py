
from PIL import Image
import numpy as np


def preprocess_image(image: Image.Image) -> np.ndarray:
    target_size = (128, 128)
    image = image.convert("RGB")
    image = image.resize(target_size)
    X = np.array(image, dtype=np.float32)    
    X = np.expand_dims(X, axis=0)  
    
    return X