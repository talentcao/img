import os
import shutil
import subprocess
import pyperclip

def main():
    # 获取用户输入的图片路径
    image_path = input("请输入图片的完整路径：")
    
    # 确保D:\img目录存在
    destination_dir = "D:\\img"
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # 获取图片文件名
    image_name = os.path.basename(image_path)
    
    # 复制图片到D:\img目录
    destination_path = os.path.join(destination_dir, image_name)
    try:
        shutil.copy(image_path, destination_path)
        print(f"图片已成功复制到 {destination_path}")
    except Exception as e:
        print(f"复制图片时发生错误：{e}")
        return
    
    # 使用Git命令提交并推送图片
    try:
        # 切换到D:\img目录
        os.chdir(destination_dir)
        os.system(f'git add {image_name}')
        os.system(f'git commit -m "添加图片 {image_name}"')
        os.system('git push')
        
        
        print("图片已成功推送到远程Git仓库")
    except subprocess.CalledProcessError as e:
        print(f"使用Git命令时发生错误：{e}")
        return

    # 将图片文件名复制到剪贴板
    pyperclip.copy(f"![{image_name}](https://ikuncao.pages.dev/{image_name})")
    print(f"图片文件名 {image_name} 已复制到剪贴板")

if __name__ == "__main__":
    main()
