import requests
hostname="http://127.0.0.1"
port=8000
base_url = "%s:%s/"%(hostname,port)
study_hall_url = base_url+"studyhall/"
# resp = requests.post(study_hall_url,json={"name":"h3","area":"h3_area"})
# print resp.status_code
#resp = requests.post(study_hall_url,json={"name":"h4","area":"h4_area"})
resp = requests.post(study_hall_url,json={"name":"wer345","area":"h4_area"})
print resp.status_code
print resp.text