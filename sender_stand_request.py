import requests
import configuration
import data

# МОЙ ПРОЕКТ 11 СПРИНТ ДИПЛОМ

# запрос на документацию API Яндекс Самокат
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# создание заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,  # подставляем полный url
                         json=body)  # тут тело

response = post_new_orders(data.orders_body)
# трек сохранен
data.answer_body["track"] = str(response.json()['track'])


# Получить заказ по его номеру
def get_orders():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDERS_PATH,
                        params= {"t": data.answer_body['track']})

response = get_orders()
