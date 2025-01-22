# 使用 Python 3.9 slim 作為基底映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔案並安裝相依套件
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼到容器中
COPY . .

# 對外開放 Flask 的埠號
EXPOSE 8080

# 啟動應用程式
CMD ["python", "app.py"]
