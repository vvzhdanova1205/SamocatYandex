import requests
import configuration
import data


# Создание нового заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# Получение номера заказа
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.STATUS_PATH,
                        params={"trackId": track})
