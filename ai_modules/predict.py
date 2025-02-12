import onnxruntime as ort
from typing import Dict
import numpy as np

onnx_model_path = "model/gender_model.onnx" 
session = ort.InferenceSession(onnx_model_path)

def predict_gender(image: np.ndarray) -> Dict[str, str]:

    images = np.vstack([image])
    inputs = {session.get_inputs()[0].name: images}
    output = session.run(None, inputs)
    prediction = output[0]
    gender = "Male" if prediction[0][0] > 0.5 else "Female"  
    return {"gender": gender}

