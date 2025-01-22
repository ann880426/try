from flask import Flask, request, jsonify, send_file
import tempfile
import os
import io
import zipfile
import openpyxl  # 用於處理 Excel 檔案

app = Flask(__name__)

@app.route('/process-file', methods=['POST'])
def process_file():
    try:
        # 接收檔案和密碼
        file = request.files['file']
        password = request.form.get('password')
        
        # 儲存檔案到暫存位置
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_file:
            temp_file.write(file.read())
            temp_filename = temp_file.name
        
        # 嘗試解密 XLSX 檔案
        try:
            # 打開受密碼保護的 Excel
            with zipfile.ZipFile(temp_filename) as zf:
                if password:
                    zf.setpassword(password.encode())
                zf.extractall(tempfile.gettempdir())
            
            # 加載解壓後的檔案內容
            extracted_file_path = os.path.join(tempfile.gettempdir(), "xl", "sharedStrings.xml")  # 修改為適合你的目標資料
            workbook = openpyxl.load_workbook(temp_filename)
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
        # 返回處理後的資料
        return jsonify({"data": data})

    finally:
        # 清理暫存檔案
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == '__main__':
    app.run(debug=True)
