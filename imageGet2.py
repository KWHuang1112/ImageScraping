import requests
import os

def download_images(image_links):
    # 创建保存图片的目录
    if not os.path.exists('images'):
        os.makedirs('images')
    
    for img_url in image_links:
        img_name = os.path.basename(img_url)
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

base_url = "https://hbhost2.imgstream2.com/file/4478/4478_"
image_links = [f"{base_url}{str(i).zfill(3)}.jpg" for i in range(1, 50)]

# 下载图片
download_images(image_links)
