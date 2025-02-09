import generator


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    COURIER_LOGIN = 'api/v1/courier/login'
    CREATE_COURIER = 'api/v1/courier'
    COURIER_DELETE = 'api/v1/courier/'
    GET_ORDER_LIST = 'api/v1/orders'
    TRACK_ORDER = '/api/v1/orders/track?t='
    CREATE_ORDER = 'api/v1/orders'
    ORDER_CANCEL = 'api/v1/orders/cancel?track='



class DataForRegistration:
    reg_data = [{'password': generator.password_generator(), 'first_name': generator.name_generator()},
                {'login': generator.login_generator(), 'first_name': generator.name_generator()}]


class DataForOrder:
    order_data = {
        "firstName": "Ira",
        "lastName": "Key",
        "address": "Winterhuder Weg",
        "metroStation": 2,
        "phone": "+7 950 000 00 00",
        "rentTime": 4,
        "deliveryDate": "2025-07-07",
        "comment": "letzte etage"
        }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]



