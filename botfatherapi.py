from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/launch/<app_name>')
def launch(app_name):
    apps = {
        'firefox': r'C:\Program Files\Mozilla Firefox\firefox.exe',
        'vscode': r'C:\Users\Egorka\AppData\Local\Programs\Microsoft VS Code\Code.exe'
    }
    subprocess.Popen(apps[app_name])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)