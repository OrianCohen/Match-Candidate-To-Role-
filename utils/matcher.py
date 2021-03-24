from models import persistence_candidates, persistence_jobs
import json


# TODO check for the most match candidate
def candidate_finder_db(job_title):
    get_job_skills = persistence_jobs.get(job_title)
    get_candidate_list = persistence_candidates.get(job_title)
    if get_candidate_list and get_job_skills:
        return get_candidate_list


# We are checking what is the skills requires for this job title, then we will check the most match candidate for
# this position
def candidate_finder_json(job_title):
    with open("./datasets/candidate.json", "r") as f:
        candidates_data = f.read()
        data_candidates = json.loads(candidates_data)

    with open("./datasets/jobs.json", "r") as f:
        jobs_data = f.read()
        data_jobs = json.loads(jobs_data)

        job_ = [element for element in data_jobs['Jobs'] if str(element['title']).lower() == str(job_title).lower()]
        if job_:
            names = [data_e for data_e in data_candidates['Candidates'] if
                     str(data_e['title']).lower() == str(job_title).lower()]

            if len(names) >= 1:
                max_skills = int(0)
                for x in names:
                    if len(x['skills']) >= max_skills:
                        max_skills = max_skills + 1
                        elemnt_end_dta = x
                        print(elemnt_end_dta)
                return elemnt_end_dta
            else:
                return names

        return ' '
