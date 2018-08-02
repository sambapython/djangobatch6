import requests
from datetime import datetime
hostname="http://127.0.0.1"
port=8000
base_url = "%s:%s/"%(hostname,port)
#study_hall_url = base_url+"studyhall/"
expense_url = base_url+"expense/"
resp = requests.post(expense_url,
					json={"studyhall":4,
					#"date":"2017-08-01",
					"desc":"createin expense",
					"value":300,
					"name":"halls10"
					}, headers={"Authorization": "Token 4975b5dc7da43dae864d0ebe7d96f2cb771558cb"})
print resp.status_code
print resp.text
resp = requests.get(expense_url,headers={"Authorization": "Token 4975b5dc7da43dae864d0ebe7d96f2cb771558cb"})
print resp.status_code
print resp.text
# print study_hall_url
# #resp = requests.get(study_hall_url)
# #study_hall_url_specific = study_hall_url+"2/"
# #study_hall_url_specific = study_hall_url+"3/"
# study_hall_url_specific = study_hall_url+"4/"
# resp = requests.put(study_hall_url_specific,
# 	json={"name":"hall2"})
# print resp
# print resp.status_code
# print resp.text

# resp = requests.get(study_hall_url_specific)
# print resp.json()

