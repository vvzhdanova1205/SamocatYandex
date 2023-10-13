#  Виктория Жданова, 8а когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Создание заказа и сохранение номера
def test_order_track():
    response_create_order  = sender_stand_request.create_new_order(data.order_body)
    # Получение трека заказа
    track = response_create_order.json().get("track")

    # Получение информации о заказе по треку
    response_get_order = sender_stand_request.get_order_track(track)
    assert response_get_order.status_code == 200
