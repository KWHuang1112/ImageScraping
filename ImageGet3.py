import requests
import os

def generate_image_links():
    base_url = "https://cc.fun8.us//2e5fc/5564/"
    image_links = []
    for page in range(242, 261):
        for img in range(1, 21):
            page_str = str(page).zfill(3)
            img_str = str(img).zfill(3)
            img_url = f"{base_url}/{page_str}/{img_str}.jpg"
            image_links.append((img_url, f"{page_str}{img_str}.jpg"))
    return image_links

def download_images(image_links):
    # 创建保存图片的目录
    if not os.path.exists('images'):
        os.makedirs('images')
    
    for img_url, img_name in image_links:
        img_path = os.path.join('images', img_name)
        
        # 下载并保存图片
        try:
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
                print(f'已下载图片: {img_path}')
        except Exception as e:
            print(f'下载图片失败: {img_url}, 错误: {e}')

# 生成图片链接列表
image_links = generate_image_links()

# 下载图片
download_images(image_links)