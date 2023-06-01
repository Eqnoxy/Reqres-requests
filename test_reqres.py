import requests

ENDPOINT = "https://reqres.in/api/"

def test_get_list_users():
    response = requests.get(ENDPOINT + "users?page=2")
    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert response.json()["data"][0]["id"] == 7
    assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"
    assert response.json()["data"][1]["id"] == 8
    assert response.json()["data"][1]["email"] == "lindsay.ferguson@reqres.in"


def test_get_single_user():
    response = requests.get(ENDPOINT + "users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"


def test_get_single_user_not_found():
    response = requests.get(ENDPOINT + "users/23")
    assert response.status_code == 404
    assert response.json() == {}


def test_list_resource():
    response = requests.get(ENDPOINT + "unknown")
    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["data"][0]["id"] == 1
    assert response.json()["data"][0]["name"] == "cerulean"
    assert response.json()["data"][1]["id"] == 2
    assert response.json()["data"][1]["name"] == "fuchsia rose"


def test_single_resource():
    response = requests.get(ENDPOINT + "unknown/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["name"] == "fuchsia rose"


def test_single_resource_not_found():
    response = requests.get(ENDPOINT + "unknown/23")
    assert response.status_code == 404
    assert response.json() == {}

def test_create():
    response = requests.post(ENDPOINT + "users", data={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201
    global mid 
    mid= response.json()["id"]
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "leader"
    assert response.json()["id"] == mid

def test_update():
    response = requests.put(ENDPOINT + "users/"+str(mid), data={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "zion resident"
    

def test_delete():
    response = requests.delete(ENDPOINT + "users/"+str(mid))
    assert response.status_code == 204
 

def test_register_successful():
    response = requests.post(ENDPOINT + "register", data={"email": "eve.holt@reqres.in","password": "pistol"})
    assert response.status_code == 200
    assert response.json()["id"] == 4
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"


def test_register_unsuccessful():
    response = requests.post(ENDPOINT + "register", data={"email": "sydney@fife"})
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_login_successful():
    response = requests.post(ENDPOINT + "login", data={"email":"eve.holt@reqres.in","password": "cityslicka"})
    assert response.status_code == 200
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"


def test_login_unsuccessful():
    response = requests.post(ENDPOINT + "login", data={"email":"peter@klaven"})
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_delayed_response():
    response = requests.get(ENDPOINT + "users?delay=3")
    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["data"][0]["id"] == 1
    assert response.json()["data"][0]["email"] == "george.bluth@reqres.in"
    

