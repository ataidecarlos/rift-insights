from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    ip = request.remote_addr
    return render_template('index.html', v_ip=ip)

if __name__ == '__main__':
    print('Before running the app')
    app.run(debug=True)
    print('After running the app')
