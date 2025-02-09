import requests
import allure
import generator

from data import Url


class TestLoginCourier:

    @allure.title("Проверка успешного логина курьера")
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and "id" in courier_id

    @allure.title("Проверка получения ошибки без создания пользователя")
    def test_unregistered_courier_login(self):
        login_data = {'login': generator.login_generator(), 'password': generator.password_generator()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_data)
        assert response.status_code == 404 and (response.json()["message"] == 'Учетная запись не найдена')

    @allure.title("Проверка ошибки без передачи пароля")
    def test_courier_login_empty_password_error(self, create_courier):
        data_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json()["message"] == "Недостаточно данных для входа")

    @allure.title("Проверка ошибки без передачи логина")
    def test_courier_login_empty_login_error(self, create_courier):
        data_response = {'login': '', 'password': create_courier[3]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json()["message"] == "Недостаточно данных для входа")