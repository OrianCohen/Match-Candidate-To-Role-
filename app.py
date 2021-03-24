from flask import Flask, render_template, request
from models import persistence_skills, persistence_candidates, persistence_jobs
from utils.matcher import candidate_finder_json

app = Flask(__name__)


# TODO need to fix JAVA_HOME argument not found
# @app.before_first_request
# def initialize_database():
    # persistence_skills.initialize()
    # persistence_jobs.initialize()
    # persistence_candidates.initialize()

@app.route('/')
def initial():
    return render_template('main.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_title = request.values['jobname']
        data_json = candidate_finder_json(job_title)
        # data_json = 'test'
        return render_template('result.html', data=data_json)
    return render_template('main.html')



if __name__ == "__main__":
    app.run()
