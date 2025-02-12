# FastAPI Gender Prediction API  

## 📌 Giới thiệu  
Đây là một API dự đoán giới tính từ hình ảnh sử dụng FastAPI.  

---

## 🔧 Cài đặt và Chạy API  

### 1️⃣ Cài đặt dependencies  
Trước tiên, hãy cài đặt thư viện cần thiết bằng lệnh:  

```bash
pip install -r requirements.txt
```

### 2️⃣ Tải mô hình từ Google Drive
Chạy script sau để tải mô hình gender_model.onnx:

```bash
python download_model.py
```

### 3️⃣ Chạy Server FastAPI
Sau khi tải model thành công, chạy API bằng lệnh sau:
```bash
python server.py
```

Mặc định, API sẽ chạy tại:
[Link local server: http://127.0.0.1:8000](http://127.0.0.1:8000)
