import requests
from jsonpath import jsonpath
from hamcrest import *


class Test_Demo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        data = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=data)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        json = {
            'level': 1,
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=json)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        headers = {
            'level': "1",
            'name': 'doulihang'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', headers=headers)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["headers"]["Name"] == "doulihang"

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        print("###################################",jsonpath(r.json(), "$..name"))
        assert jsonpath(r.json(), "$..name")[0] == "霍格沃兹测试学院公众号"

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        print("###################################",jsonpath(r.json(), "$..name"))
        assert_that(jsonpath(r.json(), "$..name")[0],equal_to("霍格沃兹测试学院公众号"))
