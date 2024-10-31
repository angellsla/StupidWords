import os

# 获取当前目录
current_directory = os.getcwd()

# 定义URL前缀
base_url = "https://sistine-1313238216.cos.ap-shanghai.myqcloud.com/pic-api/other/"

# 获取当前目录中的所有文件和目录名称
entries = os.listdir(current_directory)

# 创建输出的文件名
output_filename = f"{os.path.basename(current_directory)}.txt"

# 打开文件准备写入
with open(output_filename, 'w') as f:
    # 遍历所有文件和目录
    for entry in entries:
        # 构建完整的URL
        url = base_url + entry
        # 写入到文件中，每行一个URL
        f.write(url + '\n')

print(f"File '{output_filename}' has been created with URLs.")