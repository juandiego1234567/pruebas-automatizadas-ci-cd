from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    # Espera hasta que el elemento sea visible y lo devuelve.
    def _esperar_elemento(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            Ec.visibility_of_element_located(locator)
        )

    def navegar(self, url):
        self.driver.get(url)

    # Busca el elemento, espera a que sea visible y escribe texto.
    def escribir(self, locator, texto):
        web_element = self._esperar_elemento(locator)
        web_element.clear()
        web_element.send_keys(texto)

    # Busca el elemento, espera a que sea visible y hace clic.
    def dar_click(self, locator):
        boton = self._esperar_elemento(locator)
        boton.click()

    # Busca el elemento, espera a que sea visible y obtiene su texto.
    def obtener_texto(self, locator):
        return self._esperar_elemento(locator).text

    # Selecciona un radio button solo si aun no esta seleccionado.
    def seleccionar_radio_button(self, locator):
        radio_button = self._esperar_elemento(locator)
        if not radio_button.is_selected():
            radio_button.click()

    # Selecciona una opcion de un <select> por su texto visible.
    def select_por_texto_visible(self, locator, texto):
        elemento = self._esperar_elemento(locator)
        Select(elemento).select_by_visible_text(texto)

    # Selecciona una opcion de un <select> por su indice.
    def select_por_indice(self, locator, indice):
        elemento = self._esperar_elemento(locator)
        Select(elemento).select_by_index(indice)

    # Desplaza la pagina con JavaScript hasta que el elemento quede visible.
    def scroll_hasta_elemento(self, locator):
        elemento = self._esperar_elemento(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)

    # Devuelve True si el elemento es visible; False si no aparece a tiempo.
    def esta_visible(self, locator):
        try:
            self._esperar_elemento(locator,2)
            return True
        except TimeoutException:
            return False

    # Obtiene el valor de un atributo HTML del elemento (value, href, class...).
    def obtener_atributo(self, locator, nombre):
        return self._esperar_elemento(locator).get_attribute(nombre)

    # Espera a que todos los elementos sean visibles y devuelve una lista con ellos.
    def obtener_elementos(self, locator):
        return WebDriverWait(self.driver, 10).until(
            Ec.visibility_of_all_elements_located(locator)
        )

    def obtener_titulo_de_la_pagina(self):
        return self.driver.title

    def refrescar_pagina(self):
        self.driver.refresh()

        
