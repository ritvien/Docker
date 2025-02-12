import traceback
import io
from fastapi import File, UploadFile
from ai_modules.preprocess_image import preprocess_image
from ai_modules.predict import predict_gender
from PIL import Image

async def predict_gender_from_image(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        preprocessed_image = preprocess_image(image)
        
        result = predict_gender(preprocessed_image)
        
        return result
    
    except Exception as e:
        return {
            "error": {
                "message": str(e),
                "type": type(e).__name__,
                "args": e.args,
                "traceback": traceback.format_exc()  
            }
        }
