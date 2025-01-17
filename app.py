from flask import Flask, render_template, request, jsonify
from ocrmac import ocrmac
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 配置上传文件存储路径
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有文件'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'filename': filename})

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    filename = request.json.get('filename')
    if not filename:
        return jsonify({'error': '没有文件名'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        annotations = ocrmac.OCR(filepath).recognize()
        # 只提取文本内容，不包含坐标信息
        texts = [ann[0] for ann in annotations if isinstance(ann, tuple) and len(ann) > 0]
        return jsonify({'results': texts})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)