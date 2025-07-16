import json
import os

def save_progress(name, job_role, score, matched, missing, file_path="user_progress.json"):
    user_data = {
        "job_role": job_role,
        "score": score,
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing))
    }

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[name] = user_data

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
