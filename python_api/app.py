from flask import Flask, request, jsonify
import mysql_utils

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# url里获取参数
@app.route('/api/<username>')
def show_user_profile(username):
    return f"User: {username}"

@app.route('/api/user/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"

# get请求获取参数
@app.route('/api/get', methods=['GET'])
def get():
    print(f'params: {request.args}')
    a = request.args.get('a', default='', type=str)
    b = request.args.get('b', default='', type=str)
    result = '结果是：' + a + '999' + b
    return jsonify({"get": result})

# 表单获取参数
@app.route('/api/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Username: {username}, Password: {password}"

# post获取
@app.route('/api/post', methods=['POST'])
def post():
    data = request.get_json()
    if data:
        name = data.get('name')
        age = data.get('age')
        return f"Name: {name}, Age: {age}"
    return "No JSON received", 400

# headers参数
@app.route('/api/headers',methods=['POST'])
def api_headers():
    auth = request.headers.get('Authorization')
    token = request.headers.get('Token')
    return f"Authorization Header: {auth} Token: {token}"



#文件上传
@app.route('/api/upload', methods=['POST'])
def upload():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        filename = uploaded_file.filename
        uploaded_file.save(f"./{filename}")
        return f"File {filename} uploaded successfully!"
    return "No file uploaded", 400


@app.route('/api/getAllUsers', methods=['GET'])
def getAllUsers():
    users = mysql_utils.get_users()
    result = []
    for user in users:
        result.append({
            "username": user[1],
            "password": user[2],
            "status": user[3]
        })
    return jsonify({"users": result})

if __name__ == '__main__':
    app.run(port=5000)
