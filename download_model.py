import gdown  

file_id = "1lyUhbdEaFx1mQn5vqPIkR8rS3GNrIIa5"
url = f"https://drive.google.com/uc?id={file_id}"  
output = "model/gender_model.onnx"  

gdown.download(url, output, quiet=False)
print("Download model completed!")  
