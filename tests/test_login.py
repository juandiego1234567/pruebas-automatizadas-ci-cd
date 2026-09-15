from pages.login_page import LoginPage
from utils import config


def test_login_exitoso(login_page, driver):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    assert driver.current_url == config.URL_INVENTARIO

def test_login_fallido_credenciales_incorrectas(login_page):
    login_page.login('user_falso', '12345')
    assert login_page.mensaje_de_error_visible(), 'menage de error no mostrado'
    assert login_page.obtener_mensaje_de_error() == config.MENSAJE_LOGIN_FALLIDO, 'el mensage de error es incorrecto'

def test_login_fallido_usuario_bloqueado(login_page):
    login_page.login(config.USUARIO_BLOQUEADO, config.PASSWORD)
    assert login_page.mensaje_de_error_visible(), 'menage de error no mostrado'
    assert login_page.obtener_mensaje_de_error() == config.MENSAJE_LOGIN_FALLIDO_USUARIO_BLOQUEADO

def test_login_con_campos_vacios(login_page):
    login_page.login('', '')
    assert login_page.mensaje_de_error_visible()
    assert login_page.obtener_mensaje_de_error() == config.MENSAJE_LOGIN_FALLIDO_CAMPOS_VACIOSS

def test_login_sin_contraseña(login_page):
    login_page.login(config.USUARIO_ESTANDAR, '')
    assert login_page.mensaje_de_error_visible()
    assert login_page.obtener_mensaje_de_error() == config.MENSAJE_LOGIN_FALLIDO_CAMPOS_PASSWORD