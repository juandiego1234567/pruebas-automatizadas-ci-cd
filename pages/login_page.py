from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import config


class LoginPage(BasePage):

    input_name = (By.ID, 'user-name')
    input_password = (By.ID, 'password')
    boton_login = (By.ID, 'login-button')
    texto_error = (By.CSS_SELECTOR, '[data-test="error"]')

    def login(self, usuario, password):
        self.navegar(config.BASE_URL)
        self.escribir(self.input_name, usuario)
        self.escribir(self.input_password, password)
        self.dar_click(self.boton_login) 

    def mensaje_de_error_visible(self):
        mensaje_visible = self.esta_visible(self.texto_error)
        return mensaje_visible

    def obtener_mensaje_de_error(self):
        mensaje_de_error = self.obtener_texto(self.texto_error)
        return mensaje_de_error


    

      

    





