# Covid Tracker
An application to calculate covid risk for users where users can register and tell if they have any symptoms, travel history, or came in contact with any positive patient. Based on which application will calculate and return the risk percentage of the user.

# Technologies used
- [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

# Prerequisites
- Python3 and pip3 Installed

# Installation
- Clone repo & cd to project directory
> $ git clone ; cd covid_tracker
- Create Virtual Environment
> $ python3 -m venv {env_name}
- Install Requirements
> $ pip3 install -r requirements.txt
- Run Server
> python manage.py runserver

# User Registration API
- A user can register by providing his name, mobile number and pin code.
```
- Request
```
```
curl --request POST \
  --url http://localhost:8000/user/register \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=sCKRxvBLzXeriTqgIgdbooObKxIQYbarrF9DIFodBbMAIzZsfDy0InmfNm1BTHiP \
  --data '{
	"name": "B",
	"phoneNumber": "+919999999999",
	"pinCode": "211001"
}'
```
```
- Response
```
```
{
  "status": 200,
  "message": "Registration Successful",
  "data": {
    "userId": 3
  }
}
```
# User Admin Registration API
- Admin registration to provide admin options for the covid health workers.
```
- Request
```
```
curl --request POST \
  --url http://localhost:8000/user/admin/register \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=sCKRxvBLzXeriTqgIgdbooObKxIQYbarrF9DIFodBbMAIzZsfDy0InmfNm1BTHiP \
  --data '{
	"name": "CC",
	"phoneNumber": "+919999999999",
	"pinCode": "211001"
}'
```
```
- Response
```
```
{
  "status": 200,
  "message": "Registration Successful",
  "data": {
    "adminId": 4
  }
}
```
# User Covid Result Update API
- Health workers can enter the result of covid tests for patients.
```
- Request
```
```
curl --request PUT \
  --url http://localhost:8000/user/covid/result \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=sCKRxvBLzXeriTqgIgdbooObKxIQYbarrF9DIFodBbMAIzZsfDy0InmfNm1BTHiP \
  --data '{
	"userId": "3",
	"adminId": "4",
	"result": "positive"
}'
```
```
- Response
```
```
{
  "status": 200,
  "message": "Covid Result Updation Successful",
  "data": {
    "updated": true
  }
}
```
# User Self Assessment API
- A Users can provide few details and can see the risk of being affected by covid based on self assessment.
```
- Request
```
```
curl --request POST \
  --url http://localhost:8000/user/assessment \
  --header 'Content-Type: application/json' \
  --cookie csrftoken=sCKRxvBLzXeriTqgIgdbooObKxIQYbarrF9DIFodBbMAIzZsfDy0InmfNm1BTHiP \
  --data '{
	"userId": "1",
	"symptoms": [
		"fever",
		"cold",
		"cough"
	],
	"travelHistory": true,
	"contactWithCovidPatient": true
}'
```
```
- Response
```
```
{
  "status": 200,
  "message": "UserAssessment Recorded Successfully",
  "data": {
    "riskPercentage": 95
  }
}
```

# Check logs
> $ tail -f /tmp/covid_tracker/covid_tracker_debug.log
