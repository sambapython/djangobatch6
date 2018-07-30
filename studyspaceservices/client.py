import requests
hostname="http://127.0.0.1"
port=8000
base_url = "%s:%s/"%(hostname,port)
study_hall_url = base_url+"studyhall/"
print study_hall_url
#resp = requests.get(study_hall_url)
#study_hall_url_specific = study_hall_url+"2/"
#study_hall_url_specific = study_hall_url+"3/"
study_hall_url_specific = study_hall_url+"4/"
resp = requests.put(study_hall_url_specific,
	json={"name":"hall2"})
print resp
print resp.status_code
print resp.text

resp = requests.get(study_hall_url_specific)
print resp.json()