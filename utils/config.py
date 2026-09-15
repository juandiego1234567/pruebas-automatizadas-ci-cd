"""
Credenciales de Swag Labs según el tipo de usuario (estándar, bloqueado, con problemas, lento).
"""

BASE_URL = 'https://www.saucedemo.com/'
URL_INVENTARIO = 'https://www.saucedemo.com/inventory.html'


# Datos de prueba para la pagina de Login

PASSWORD = 'secret_sauce'

USUARIO_ESTANDAR = 'standard_user'
USUARIO_BLOQUEADO = 'locked_out_user'
USUARIO_CON_PROBLEMAS = 'problem_user'
USUARIO_LENTO = 'performance_glitch_user'

MENSAJE_LOGIN_FALLIDO = 'Epic sadface: Username and password do not match any user in this service'
MENSAJE_LOGIN_FALLIDO_USUARIO_BLOQUEADO = 'Epic sadface: Sorry, this user has been locked out.'
MENSAJE_LOGIN_FALLIDO_CAMPOS_VACIOSS = 'Epic sadface: Username is required'
MENSAJE_LOGIN_FALLIDO_CAMPOS_PASSWORD = 'Epic sadface: Password is required'


# Datos para la pagina de Productos

TITULO = 'Swag Labs'
CANTIDAD_PRODUCTOS = 6


# Datos del producto Sauce Labs Bike Light 

NOMBRE_PRODUCTO = "Sauce Labs Backpack"
DESCRIPCION_PRODUCTO = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
PRECIO_PRODUCTO = 29.99
URL_PRODUCTO = "https://www.saucedemo.com/inventory-item.html?id=4"