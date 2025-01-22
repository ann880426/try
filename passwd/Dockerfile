# 使用官方 Python 基底映像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製程式碼到容器
COPY . .

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 暴露埠 8080，Cloud Run 預設使用此埠
EXPOSE 8080

# 啟動應用程式
CMD ["python", "main.py"]
