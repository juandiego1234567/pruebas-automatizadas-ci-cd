from utils import config
import pytest


def test_mostrar_productos_tras_iniciar_sesion(login_page, product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    assert product_page.obtener_cantidad_de_productos() == config.CANTIDAD_PRODUCTOS, 'La cantidad de producto no es la esperada'


def test_agregar_producto_al_carrito(login_page, product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    product_page.agregar_producto("Sauce Labs Backpack", "Add to cart")
    assert product_page.cantidad_productos() == '1', 'la cantidad de productos agregadas al carrito no es correcta'


def test_quitar_un_producto_desde_el_inventario(login_page, product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    product_page.agregar_producto('Sauce Labs Backpack', 'Add to cart')
    product_page.quitar_producto("Sauce Labs Backpack", 'Remove')
    assert not product_page.validar_contador(), 'el contador no desapareció tras quitar el producto'
    assert product_page.obtener_texto_button('Sauce Labs Backpack') == 'Add to cart', 'el botón no volvió a Add to cart tras quitar el producto'
    

def test_ordenar_productos_por_precio(login_page, product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    product_page.ordenar_productos("Price (low to high)")
    precios = product_page.obtener_lista_de_precios()
    assert precios == sorted(precios), 'Los precios no estan ordenados de menor a mayor'


def test_ordenar_productos_alfabeticamente(login_page, product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    product_page.ordenar_productos("Name (A to Z)")
    nombres_de_productos = product_page.obtner_lista_de_nombres_productos()
    assert nombres_de_productos == sorted(nombres_de_productos), 'Los productos no estan ordenados alfabeticamente'

@pytest.mark.ui
def test_ver_detalles_de_un_producto(login_page,product_page):
    login_page.login(config.USUARIO_ESTANDAR, config.PASSWORD)
    product_page.ver_detalles_de_un_producto("Sauce Labs Backpack")
    assert product_page.driver.current_url == config.URL_PRODUCTO
    nombre, descripcion, precio = product_page.obtener_detalles_de_un_producto()
    assert nombre == config.NOMBRE_PRODUCTO, 'El nombre del producto no es el esperado'
    assert descripcion == config.DESCRIPCION_PRODUCTO, 'La descripcion del producto no es la esperada'
    assert precio == config.PRECIO_PRODUCTO, 'El precio del producto no es el esperado'