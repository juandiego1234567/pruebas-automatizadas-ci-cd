from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    productos = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    contador_carrito = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    titulo = (By.CLASS_NAME, 'title')
    filtar_productos = (By.CLASS_NAME, "product_sort_container")
    precios = (By.CLASS_NAME, "inventory_item_price")
    nombre_producto = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    descripcion_producto = (By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')
    precio_producto = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')

    def obtener_cantidad_de_productos(self):
        lista_de_productos = self.obtener_elementos(self.productos)
        return len(lista_de_productos)

    def obtener_titulo_de_pagina_productos(self):
        return self.obtener_titulo_de_la_pagina()

    def gestionar_producto(self, nombre_producto, text_button):
        button_xphat = f"//div[@class='inventory_item'][.//div[normalize-space()='{nombre_producto}']]//button[normalize-space()='{text_button}']"
        button = self._esperar_elemento((By.XPATH, button_xphat))
        button.click()

    def agregar_producto(self, nombre_producto, text_button):
        self.gestionar_producto(nombre_producto, text_button)

    def quitar_producto(self, nombre_producto, text_button):
        self.gestionar_producto(nombre_producto, text_button)

    def obtener_texto_button(self, nombre_producto):
        button_xphat = f"//div[@class='inventory_item'][.//div[normalize-space()='{nombre_producto}']]//button"
        button = self._esperar_elemento((By.XPATH, button_xphat))
        return button.text

    def cantidad_productos(self):
        return self.obtener_texto(self.contador_carrito)

    def validar_contador(self):
        return self.esta_visible(self.contador_carrito)

    def ordenar_productos(self,texto):
        self.select_por_texto_visible(self.filtar_productos, texto) 

    def obtener_lista_de_precios(self):
        precios = self.obtener_elementos(self.precios)
        lista_de_precios = [float(precio.text.replace("$", "")) for precio in precios]
        return lista_de_precios

    def obtner_lista_de_nombres_productos(self):
        nombres = self.obtener_elementos(self.productos)
        nombres_productos = [nombre_producto.text for nombre_producto in nombres]
        return nombres_productos 

    def ver_detalles_de_un_producto(self, nombre_producto):
        elemteto_xphat = f"//div[@class='inventory_item'][.//div[normalize-space()='{nombre_producto}']]//a"
        link_detalle_producto = self._esperar_elemento((By.XPATH, elemteto_xphat))
        link_detalle_producto.click()

    def obtener_detalles_de_un_producto(self):
        nombre = self.obtener_texto(self.nombre_producto)
        descripcion = self.obtener_texto(self.descripcion_producto)
        precio = float(self.obtener_texto(self.precio_producto).replace("$",""))
        return nombre, descripcion, precio

    
        

    

        

    

   


