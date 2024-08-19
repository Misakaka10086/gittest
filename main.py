# just a test for the github
# 创建一个基于flask的web应用，显示hello world
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html', message1='Hello World!', message2='What a brave new world this is!')



# 启动应用
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4001, debug=True)
