import os
import re
import urllib.request
from tqdm import tqdm

# 定义一个函数来处理Markdown文件
def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式来查找Markdown文件中的图片链接
    img_links = re.findall(r'!\[.*?\]\((http[s]?://.*?)\)', content)

    if img_links:
        # 创建一个目录来存储下载的图片
        img_dir = os.path.join(os.path.dirname(file_path), 'img')
        os.makedirs(img_dir, exist_ok=True)

        total_images = len(img_links)

        for i, img_link in enumerate(img_links, start=1):
            # 处理包含?source=*的图片链接
            img_link = img_link.split('?source=')[0]

            try:
                # 获取图片文件名
                img_filename = os.path.basename(img_link)

                # 下载图片到img目录
                img_path = os.path.join(img_dir, img_filename)
                urllib.request.urlretrieve(img_link, img_path)

                # 更新Markdown文件中的图片链接为本地相对路径
                content = content.replace(img_link, f'img/{img_filename}')
            except Exception as e:
                print(f"Error downloading {img_link}: {str(e)}")

        # 保存更新后的Markdown内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

# 遍历指定目录及其子目录下的所有Markdown文件
def process_markdown_files_in_directory(root_dir):
    markdown_files = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))

    total_markdown_files = len(markdown_files)

    for i, markdown_file in tqdm(enumerate(markdown_files, start=1), total=total_markdown_files, desc='Processing Markdown Files'):
        process_markdown_file(markdown_file)

# 指定要处理的根目录
root_directory = './posts'

# 调用函数处理Markdown文件
process_markdown_files_in_directory(root_directory)
