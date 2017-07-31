from flask import Flask
from flask import request

app = Flask(__name__);


@app.route("/" , methods=['GET' , 'POST'])
def home():
    return '<h1>我是Home界面</h1>';

@app.route("/signin" , methods=["GET"])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>''';

@app.route("/signin" , methods=["POST"])
def signin():
    if request.form["username"] == "admin" and request.form["password"] == "password":
        return "<h1>你好  用户</h1>";
    else:
        return "<h1>用户名/密码 错误</h1>";

if __name__ == "__main__":
    app.run();

print(app);