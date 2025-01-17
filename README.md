# ocr-md-renderer
一个基于 macOS 原生 OCR 功能的文字识别工具，使用 Flask 构建 Web 界面。

## 功能特点

- 支持拖拽上传图片或点击选择图片
- 使用 macOS 原生 OCR 功能，无需额外安装 OCR 引擎
- 识别结果支持行选择和复制
- 简洁美观的用户界面
- 支持中英文识别

## 系统要求

- macOS 系统
- Python 3.7+

## 安装

1. 克隆项目：
```bash
git clone https://github.com/senzi/ocr-md-renderer.git
cd ocr-md-renderer
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 启动服务器：
```bash
python app.py
```

2. 在浏览器中打开：`http://localhost:5000`

3. 使用方式：
   - 拖拽图片到上传区域，或点击"选择文件"按钮
   - 点击"开始识别"按钮进行文字识别
   - 识别结果显示后，可以：
     - 点击单行选中/取消选中
     - 点击复制按钮复制选中内容（未选中时复制全部）
   - 点击"重新上传"可以重新选择图片

## 文件说明

- `app.py`: 主应用程序
- `templates/index.html`: 前端界面
- `static/uploads/`: 上传文件临时存储目录
- `requirements.txt`: 项目依赖
