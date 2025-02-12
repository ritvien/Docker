# Sử dụng image cơ sở là python 3.9 nhỏ gọn
FROM python:3.9-slim

# Thiết lập folder làm việc
WORKDIR /app

# Copy file yêu cầu (dependencies) vào container
# Sử dụng requirements.txt khi các package chỉ dùng pip, base image là python.
# Nếu cần quản lý các kênh khác nhau, dependencies lồng nhau,
# sử dụng Conda để quản lý môi trường, cần cài đặt các package hệ thống
# làm việc với các thư viện AI/ML thì nên dùng environment.yml
COPY requirements.txt /app/

# Cài đặt dependencies (--no-cache-dir làm nhẹ image)
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code vào container

COPY . /app/

# Chạy file tải model trong quá trình build
RUN python download_model.py

# Mở cổng 8000
EXPOSE 8000

# Chạy ứng dụng khi container khởi động
CMD ["python", "server.py"]