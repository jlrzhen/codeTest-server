from flask import Flask, render_template
import requests, time, endpoints
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/<user>/<repo>")
def submit(user, repo):
    f = open("repo", "w")
    f.write('{remote}/{user}/{repo}'.format(remote=endpoints.remote_repo, user=user, repo=repo))
    f.close()
    requests.get(endpoints.trigger_build)
    time.sleep(5)
    f2 = open("repo", "w")
    f2.write('')
    f2.close() 
    return render_template('submit.html', user=user, repo=repo, remote_repo=endpoints.remote_repo, console_output=endpoints.console_output, homepage=endpoints.homepage)
