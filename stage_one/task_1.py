from flask import Flask, request, jsonify
from datetime import date, datetime

app = Flask(__name__)

current_day = date.today()
utc_time = datetime.now().isoformat(timespec='seconds') + 'Z'
github_file_url = 'https://github.com/holic65/HNGX-Backend_Track/stage_one/task_1.py'
github_repo_url = 'https://github.com/holic65/HNGX-Backend_Track'


@app.route('/', methods=['GET'])
def home():
    return 'Welcome To My First Task in HNGX'


@app.route('/api', methods=['GET'])
def api():
    args = request.args
    hng_params = {
        "slack_name": args.get('slack_name'),
        "current_day": current_day.strftime("%A"),
        "utc_time": utc_time,
        "track": args.get('track'),
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(hng_params)

if __name__ == '__main__':
    app.run()
