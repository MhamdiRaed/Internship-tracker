import requests

url = "https://remotive.com/api/remote-jobs"

response = requests.get(url)
items = response.json()

KEYWORDS = ["intern", "internship", "junior", "trainee", "graduate"]

def is_relevant(job):
    return any(k in job["title"].lower() for k in KEYWORDS)

def normalize(job):
    return {
        "title": job["title"],
        "company": job["company_name"],
        "country": job["candidate_required_location"],
        "remote": True,
        "url": job["url"]
    }

jobs = items["jobs"]

filtered = [job for job in jobs if is_relevant(job)]

clean = [normalize(job) for job in filtered]

print(clean[0] if clean else "no matches found")