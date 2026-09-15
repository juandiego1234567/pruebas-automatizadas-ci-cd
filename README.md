# Proyecto de pruebas automatizadas - Swag Labs

Automatización de pruebas del login de [Swag Labs](https://www.saucedemo.com/) usando **Selenium WebDriver**, **pytest** y el patrón de diseño **Page Object Model (POM)**.

## Estructura

```
proyecto/
├── pages/          # Page Objects (elementos y acciones de cada página)
│   ├── base_page.py
│   └── login_page.py
├── tests/          # Casos de prueba
│   └── test_login.py
├── utils/          # Configuración (URLs, credenciales)
│   └── config.py
├── conftest.py     # Fixtures de pytest (driver)
├── pytest.ini      # Configuración de pytest
└── requirements.txt
```

## Ejecución

Desde la raíz del proyecto:

```bash
pytest -v
```

Para correr un archivo específico:

```bash
pytest tests/test_login.py -v
```

## Métodos disponibles (BasePage)

`BasePage` contiene las acciones genéricas que **todas** las páginas heredan. Cada método recibe un `locator` (una tupla como `(By.ID, 'user-name')`).

### `escribir(locator, texto)`
Escribe texto en un campo `input` o `textarea`, esperando primero a que el elemento sea visible.

**Cuándo usarlo:** siempre que una prueba necesite **rellenar datos en un formulario**: usuario, contraseña, correo, búsquedas, comentarios, direcciones, etc. Es tu método principal para simular a un usuario escribiendo.

```python
def test_escribir_usuario(driver):
    login = LoginPage(driver)
    login.escribir(login.imput_name, "standard_user")
```

### `dar_click(locator)`
Hace clic en un elemento, esperando primero a que sea visible.

**Cuándo usarlo:** cada vez que la prueba deba **presionar algo**: botones de enviar/login, enlaces de navegación, íconos, pestañas o checkboxes. Es la acción más frecuente para avanzar en un flujo.

```python
def test_click_login(driver):
    login = LoginPage(driver)
    login.dar_click(login.boton_login)
```

### `obtener_texto(locator)`
Devuelve el **texto visible** de un elemento.

**Cuándo usarlo:** cuando necesites **verificar que un texto en pantalla es exactamente el esperado**: mensajes de error, títulos, nombres de producto, totales, confirmaciones. Es la base de muchos `assert` de contenido.

```python
def test_mensaje_error(driver):
    login = LoginPage(driver)
    login.login("malo", "malo")
    assert login.obtener_texto(login.texto_error) == "Epic sadface: Username and password do not match any user in this service"
```

### `seleccionar_opcion(locator)`
Selecciona un **radio button** solo si aún no está marcado (evita clics innecesarios). También sirve para asegurar que un **checkbox** quede marcado.

**Cuándo usarlo:** en pruebas de **formularios con opciones**: elegir género, tipo de envío, forma de pago, aceptar términos. Lo usas cuando debes garantizar que una opción quede seleccionada sin arriesgarte a desmarcarla.

```python
def test_elegir_genero(driver):
    pagina = RegistroPage(driver)
    pagina.seleccionar_opcion(pagina.genero_masculino)
```

### `seleccionar_por_texto(locator, texto)`
Selecciona una opción de un menú desplegable `<select>` por el **texto que ve el usuario**.

**Cuándo usarlo:** siempre que la prueba deba **elegir un valor de una lista desplegable**: país, ciudad, cantidad, categoría, moneda. Ideal cuando conoces el texto que aparece en pantalla, no el valor interno.

```python
def test_elegir_pais(driver):
    pagina = RegistroPage(driver)
    pagina.seleccionar_por_texto(pagina.pais, "Colombia")
```

### `scroll_hasta_elemento(locator)`
Desplaza la página (con JavaScript) hasta que el elemento quede a la vista.

**Cuándo usarlo:** cuando un elemento está **fuera de la pantalla** y el clic normal falla, o en **páginas largas** (checkout, listados). Suele usarse justo antes de un `dar_click` para asegurar que el elemento esté visible.

```python
def test_ir_al_boton_final(driver):
    checkout = CheckoutPage(driver)
    checkout.scroll_hasta_elemento(checkout.boton_finalizar)
    checkout.dar_click(checkout.boton_finalizar)
```

### `esta_visible(locator)`
Devuelve `True` si el elemento es visible, o `False` si no aparece a tiempo (sin romper la prueba).

**Cuándo usarlo:** cuando solo te importa **si algo aparece o desaparece**, sin revisar su texto: que salga un mensaje de error, un popup, un spinner, una notificación, o que un elemento **ya no** esté tras una acción. Perfecto para `assert` de tipo verdadero/falso.

```python
def test_aparece_error(driver):
    login = LoginPage(driver)
    login.login("malo", "malo")
    assert login.esta_visible(login.texto_error)        # debe aparecer
```

### `obtener_atributo(locator, nombre)`
Devuelve el valor de un **atributo HTML** del elemento (`value`, `href`, `class`, `src`, etc.).

**Cuándo usarlo:** cuando necesites **validar información interna del HTML**, no el texto visible: el `href` de un enlace, el `value` que quedó en un campo, la clase CSS que indica un estado (ej. `error`), o el `src` de una imagen.

```python
def test_link_ayuda(driver):
    pagina = HomePage(driver)
    url = pagina.obtener_atributo(pagina.enlace_ayuda, "href")
    assert url == "https://ayuda.miapp.com"
```

### Resumen rápido

| Método | Qué hace | Se usa para |
|---|---|---|
| `escribir(locator, texto)` | Escribe en input/textarea | Llenar formularios |
| `dar_click(locator)` | Hace clic | Botones, enlaces |
| `obtener_texto(locator)` | Lee el texto visible | Verificar mensajes exactos |
| `seleccionar_opcion(locator)` | Marca un radio/checkbox | Formularios de opción |
| `seleccionar_por_texto(locator, texto)` | Elige opción de un `<select>` | Menús desplegables |
| `scroll_hasta_elemento(locator)` | Baja hasta el elemento (JS) | Elementos fuera de pantalla |
| `esta_visible(locator)` | `True`/`False` si aparece | Verificar aparición |
| `obtener_atributo(locator, nombre)` | Lee un atributo HTML | Validar `href`, `value`, etc. |

## Credenciales de prueba

| Usuario | Contraseña |
|---|---|
| `standard_user` | `secret_sauce` |

