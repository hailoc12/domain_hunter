# Sử dụng image Python 3.9 làm base
FROM python:3.9

# Đặt thư mục làm thư mục làm việc
WORKDIR /app

# Sao chép các tệp cần thiết vào container
COPY . .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 của Django
EXPOSE 8000

# Chạy lệnh khởi động Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

