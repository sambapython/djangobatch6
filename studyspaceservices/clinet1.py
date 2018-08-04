import requests
from datetime import datetime
hostname="http://127.0.0.1"
port=8000
base_url = "%s:%s/"%(hostname,port)
study_hall_url = base_url+"studyhall/"
resp = requests.post(study_hall_url,
	json={"name":"anjaneyanagarstudyhall","area":"ameerpet"})
print resp
print resp.status_code
print resp.text
