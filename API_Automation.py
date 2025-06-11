
import requests
import random
import json
import string

#base URL:
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer 01aac109247d548be47e33b7f56048cf3b7e8485354cc937bbaa432fa3e5551f"


#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#GET Request

def get_request():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token} #use of dictionary here, authorisation will be called and token value will be passed
    response = requests.get(url, headers=headers)
    print("get url:" + url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body:",json_str)





#POST Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Testing API Automation_python",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }

    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body:" , json_str)
    user_id = json_data["id"]
    print("user_id==>",user_id)
    assert "name" in json_data
    #assert json_data["name"] == "Testing API Automation123"
    return user_id






#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Testing API Automation in updated Body python",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body:" , json_str)
    assert json_data["id"] == user_id
    #assert json_data["name"] == "Testing API Automation using python"





#DELETE Requests
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("delete url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(">>>>>Delete user is done")


def get_request_Id(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {
        "Authorization": auth_token}  # use of dictionary here, authorisation will be called and token value will be passed
    response = requests.get(url, headers=headers)
    print("get_ID url:" + url)
    assert response.status_code == 404 #404 is for when user is deleted and we want to retreive it.
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body:", json_str)


#cAlling Requestes
#get_request()  #this get request retrieves all the data
user_id = post_request()
put_request(user_id)
delete_request(user_id)
get_request_Id(user_id) #always change the response code according to the response we want
