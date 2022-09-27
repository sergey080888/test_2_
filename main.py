import requests

token = ''
url = "https://cloud-api.yandex.net/v1/disk/resources?path=1"


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


def creating_folfer():
    response = requests.put(url=url, headers=get_headers())
    response_ = requests.get(url=url, headers=get_headers())
    return response.status_code, response_.status_code


def deleting_folder():
    url_ = 'https://cloud-api.yandex.net/v1/disk/resources?path=1&permanently=true'
    response = requests.delete(url=url_, headers=get_headers())
    return response.status_code


if __name__ == '__main__':
    print(creating_folfer())
