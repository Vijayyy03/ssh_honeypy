from flask import Flask, render_template
from dashboard_data_parser import get_credentials, get_commands, get_http_logs

app = Flask(__name__)

@app.route("/")
def dashboard():
    creds = get_credentials()
    cmds = get_commands()
    http_logs = get_http_logs()
    return render_template("dashboard.html", creds=creds, cmds=cmds, http_logs=http_logs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
