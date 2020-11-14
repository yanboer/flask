from flask import escape
from flask import Flask

app = Flask(__name__)

# 可以绑定多个 url
@app.route("/")
@app.route("/home")
@app.route("/hello")
def hello():
    return "<h1>Hello First Flask</h1>"


@app.route("/user/<username>")
def user_page(username):
    # 用 Flask 提供的 escape() 函数对 username 变量进行转义处理
    return "User : %s" % escape(username)

if __name__ == "__main__":
    app.run(debug=True)
