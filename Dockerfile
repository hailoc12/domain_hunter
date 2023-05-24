# Sử dụng image Python 3.9 làm base
FROM python:3.9

# Đặt thư mục làm thư mục làm việc
WORKDIR /app

# Sao chép các tệp cần thiết vào container
COPY . .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Chạy lệnh khởi động Django server
CMD ["python", "gradio_app.py"]

