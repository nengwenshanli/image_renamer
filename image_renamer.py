import os
from tkinter import Tk, filedialog
from PIL import Image
import easyocr
import requests
import json
import numpy as np

# 初始化 EasyOCR 读取器
reader = easyocr.Reader(['ch_sim', 'en'])  # 支持中文简体和英文

def select_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def perform_ocr(image_path):
    try:
        # 使用PIL打开图像并转换为RGB模式
        with Image.open(image_path).convert('RGB') as img:
            # 将PIL图像转换为numpy数组
            img_array = np.array(img)
        
        result = reader.readtext(img_array)
        text = ' '.join([item[1] for item in result])
        return text
    except Exception as e:
        print(f"OCR处理失败: {str(e)}")
        return ""



def get_ai_summary(text):
    api_key = 'sk-b546058d2afc42a1899ca9e0c6c46'#your api_key,this key is wrong,please change to your api_key
    api_url = 'https://api.deepseek.com/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个助手，需要总结给定的文本。请用简洁的短语(长度不超过10个字)概括文本的主要内容。"},
            {"role": "user", "content": f"请总结以下文本:\n{text}"}
        ],
        "stream": False
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        summary = result['choices'][0]['message']['content'].strip()
        return summary
    except requests.exceptions.RequestException as e:
        print(f"AI API请求失败: {e}")
        return "无法获取摘要"

def rename_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(folder_path, filename)
            
            try:
                # 执行OCR
                print(f"开始OCR处理: {filename}")
                ocr_text = perform_ocr(file_path)
                if not ocr_text:
                    print(f"跳过 {filename}: OCR未能提取文本")
                    continue
                print(f"OCR处理完成: {filename}, 提取文本长度: {len(ocr_text)}")

                # 获取AI摘要
                print(f"开始AI总结: {filename}")
                summary = get_ai_summary(ocr_text)
                if not summary:
                    print(f"跳过 {filename}: 无法获取AI摘要")
                    continue
                print(f"AI总结完成: {filename}, 总结长度: {len(summary)}")

                # 生成新文件名
                new_filename = f"{summary[:50]}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(folder_path, new_filename)
                
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"已重命名: {filename} -> {new_filename}")
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")
                continue  # 继续处理下一个文件

if __name__ == "__main__":
    folder_path = select_folder()
    if folder_path:
        rename_images(folder_path)
        print("重命名完成!")
    else:
        print("未选择文件夹,程序退出。")
