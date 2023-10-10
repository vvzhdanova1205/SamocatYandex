#  Виктория Жданова, 8а когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                    json=body,
                    headers=data.headers)


response = post_new_order(data.order_body)
print(response.status_code)
print(response.text)


def get_new_track_number():
    order_body = data.order_body
    response_order = post_new_order(order_body)
    response_json = response_order.json()
    if "trackNumber" in response_json:
        return response_json["trackNumber"]
    else:
        return "Track number not available in response"


def get_order_status(track_number):
    url = configuration.URL_SERVICE + configuration.STATUS_PATH + f"/{track_number}"
    response = requests.get(url)
    response_json = response.json()
    if "status" in response_json:
        return response_json["status"]
    else:
        return "Status not available in response"


# Создание нового заказа и получение трек-номера
new_track_number = get_new_track_number()
print("New Track Number:", new_track_number)

# Получение статуса заказа по трек-номеру
order_status = get_order_status(new_track_number)
print("Order Status:", order_status)
