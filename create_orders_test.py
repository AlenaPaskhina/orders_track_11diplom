import sender_stand_request
import data
#Выполнить запрос на создание заказа.
#Сохранить номер трека заказа.
#Выполнить запрос на получения заказа по треку заказа.
#Проверить, что код ответа равен 200.

# АЛЕНА ПАСХИНА, 11-Й ПОТОК — Финальный проект. Инженер по тестированию плюс
# успешное создание заказа
def test_success_create_orders():
# в переменную orders_response сохраняем результат создания заказа
    orders_response = sender_stand_request.post_new_orders(data.orders_body)
# Проверяется, что код ответа равен 201
    assert orders_response.status_code == 201
# Проверяется, что в ответе есть поле 'track', и оно не пустое
    assert orders_response.json()['track'] != ""

# В переменную orders_body_response сохраняется результат запроса на получение заказа
    orders_body_response = sender_stand_request.get_orders()
# Проверяется, что код ответа равен 200
    assert orders_body_response.status_code == 200


