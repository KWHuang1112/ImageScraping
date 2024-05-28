import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re
import string

def clean_filename(filename):
    # 移除非法字符
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    cleaned_filename = ''.join(c for c in filename if c in valid_chars)
    return cleaned_filename

# 目標URL
#url = 'http://example.com'
url ='https://18h.mm-cg.com/zh/#18H_content/8121/content.html'

# 發送HTTP請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析HTML內容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 建立保存圖片的目錄
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # 獲取所有圖片標籤
    img_tags = soup.find_all('img')
    for img in img_tags:
        # 獲取圖片的URL
        img_url = img.get('src')
        
        # 處理相對URL
        img_url = urljoin(url, img_url)
        
        # 獲取圖片的名稱
        img_name = os.path.basename(img_url)
        
        # 清理圖片名稱
        img_name = clean_filename(img_name)
        
        img_path = os.path.join('images', img_name)
        
        # 下載並保存圖片
        try:
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
                print(f'已下載圖片: {img_path}')
        except Exception as e:
            print(f'下載圖片失敗: {img_url}, 錯誤: {e}')
else:
    print(f'請求失敗，狀態碼: {response.status_code}')
