import requests
hostname="http://127.0.0.1"
port=8000
base_url = "%s/%s/"%(hostname,port)
study_hall_url = base_url+"studyhall/"
print study_hall_url
resp = requests.get(study_hall_url)
print resp