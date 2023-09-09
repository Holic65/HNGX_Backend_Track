from flask import Flask, request, jsonify
from datetime import date, datetime

app = Flask(__name__)

current_day = date.today()
utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
github_file_url = 'https://github.com/Holic65/HNGX_Backend_Track/blob/master/stage_one/task_1.py'
github_repo_url = 'https://github.com/Holic65/HNGX_Backend_Track/'


@app.route('/', methods=['GET'])
def home():
    return 'Welcome To My First Task in HNGX'


@app.route('/api', methods=['GET'])
def api():
    args = request.args
    hng_params = {
        "slack_name": args.get('slack_name'),
        "current_day": current_day.strftime("%A"),
        "utc_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": args.get('track'),
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(hng_params)
