# Casos de prueba - Automatización de Swag Labs

Documento de casos de prueba para la automatización de la aplicación **[Swag Labs](https://www.saucedemo.com/)**.

El objetivo es automatizar la aplicación **completa** (login, inventario, carrito y checkout). El trabajo se realiza por módulos; **se comienza por el módulo de Login** y luego se avanza al resto.

## Información general

| Dato | Valor |
|---|---|
| Aplicación | Swag Labs |
| URL | https://www.saucedemo.com/ |
| Herramientas | Selenium WebDriver, pytest, Page Object Model |
| Navegador | Google Chrome |

## Datos de prueba

| Usuario | Contraseña | Comportamiento |
|---|---|---|
| `standard_user` | `secret_sauce` | Login exitoso |
| `locked_out_user` | `secret_sauce` | Usuario bloqueado |
| `problem_user` | `secret_sauce` | Login exitoso (con errores de UI) |
| `performance_glitch_user` | `secret_sauce` | Login exitoso (lento) |

## Estado de los módulos

| Módulo | Estado |
|---|---|
| Login | Automatizado |
| Inventario / Productos | Documentado |
| Carrito | Documentado |
| Checkout | Documentado |

---

## Módulo: Login

### TC-01 - Login exitoso con usuario estándar
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Datos** | `standard_user` / `secret_sauce` |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Escribir `standard_user` en el campo Usuario<br>3. Escribir `secret_sauce` en el campo Contraseña<br>4. Hacer clic en el botón Login |
| **Resultado esperado** | El sistema redirige a la página de inventario (`/inventory.html`) |
| **Prioridad** | Alta |

### TC-02 - Login fallido con credenciales incorrectas
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Datos** | `usuario_invalido` / `clave_invalida` |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Escribir un usuario inexistente en el campo Usuario<br>3. Escribir una contraseña incorrecta en el campo Contraseña<br>4. Hacer clic en el botón Login |
| **Resultado esperado** | Se muestra el mensaje: *"Epic sadface: Username and password do not match any user in this service"* |
| **Prioridad** | Alta |

### TC-03 - Login con usuario bloqueado
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Datos** | `locked_out_user` / `secret_sauce` |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Escribir `locked_out_user` en el campo Usuario<br>3. Escribir `secret_sauce` en el campo Contraseña<br>4. Hacer clic en el botón Login |
| **Resultado esperado** | Se muestra el mensaje: *"Epic sadface: Sorry, this user has been locked out."* |
| **Prioridad** | Alta |

### TC-04 - Login con campos vacíos
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Datos** | Usuario vacío / Contraseña vacía |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Dejar el campo Usuario vacío<br>3. Dejar el campo Contraseña vacío<br>4. Hacer clic en el botón Login |
| **Resultado esperado** | Se muestra el mensaje: *"Epic sadface: Username is required"* |
| **Prioridad** | Media |

### TC-05 - Login sin contraseña
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Datos** | `standard_user` / Contraseña vacía |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Escribir `standard_user` en el campo Usuario<br>3. Dejar el campo Contraseña vacío<br>4. Hacer clic en el botón Login |
| **Resultado esperado** | Se muestra el mensaje: *"Epic sadface: Password is required"* |
| **Prioridad** | Media |

---

## Módulo: Inventario / Productos

### TC-06 - Mostrar los productos tras iniciar sesión
| Campo | Detalle |
|---|---|
| **Precondición** | El navegador está abierto |
| **Pasos** | 1. Navegar a `https://www.saucedemo.com/`<br>2. Iniciar sesión con `standard_user` / `secret_sauce`<br>3. Observar la lista de productos del inventario |
| **Resultado esperado** | Se muestran los 6 productos disponibles |
| **Prioridad** | Alta |

### TC-07 - Agregar un producto al carrito
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Ubicar el producto "Sauce Labs Backpack"<br>2. Hacer clic en su botón "Add to cart"<br>3. Observar el contador del carrito y el botón del producto |
| **Resultado esperado** | El contador del carrito muestra `1` y el botón del producto cambia a "Remove" |
| **Prioridad** | Alta |

### TC-08 - Quitar un producto desde el inventario
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Agregar el producto "Sauce Labs Backpack" con "Add to cart"<br>2. Hacer clic en el botón "Remove" del mismo producto<br>3. Observar el contador del carrito y el botón del producto |
| **Resultado esperado** | El contador del carrito desaparece y el botón vuelve a "Add to cart" |
| **Prioridad** | Media |

### TC-09 - Ordenar productos de la A a la Z
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Abrir el menú de ordenamiento (esquina superior derecha)<br>2. Seleccionar la opción "Name (A to Z)"<br>3. Observar el orden de los productos |
| **Resultado esperado** | Los productos se muestran ordenados alfabéticamente de la A a la Z |
| **Prioridad** | Media |

### TC-10 - Ordenar productos por precio (menor a mayor)
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Abrir el menú de ordenamiento (esquina superior derecha)<br>2. Seleccionar la opción "Price (low to high)"<br>3. Observar el orden de los precios |
| **Resultado esperado** | Los productos se muestran del precio más bajo al más alto |
| **Prioridad** | Media |

### TC-11 - Ver el detalle de un producto
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Hacer clic en el nombre del producto "Sauce Labs Backpack"<br>2. Observar la página de detalle |
| **Resultado esperado** | Se abre la página de detalle con nombre, descripción y precio del producto |
| **Prioridad** | Media |

### TC-12 - Cerrar sesión desde el menú
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario tiene una sesión activa |
| **Pasos** | 1. Hacer clic en el botón del menú lateral (☰)<br>2. Hacer clic en la opción "Logout"<br>3. Observar la página resultante |
| **Resultado esperado** | El usuario regresa a la página de login |
| **Prioridad** | Alta |

## Módulo: Carrito

### TC-13 - Mostrar los productos agregados en el carrito
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario inició sesión y está en la página de inventario |
| **Pasos** | 1. Agregar el producto "Sauce Labs Backpack" con "Add to cart"<br>2. Hacer clic en el ícono del carrito (esquina superior derecha)<br>3. Observar la lista del carrito |
| **Resultado esperado** | El carrito muestra los productos agregados con su nombre y precio |
| **Prioridad** | Alta |

### TC-14 - Eliminar un producto desde el carrito
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario tiene un producto agregado y está en la página del carrito |
| **Pasos** | 1. Ubicar el producto en la lista del carrito<br>2. Hacer clic en su botón "Remove"<br>3. Observar la lista del carrito |
| **Resultado esperado** | El producto desaparece de la lista del carrito |
| **Prioridad** | Alta |

### TC-15 - Continuar comprando
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario está en la página del carrito |
| **Pasos** | 1. Hacer clic en el botón "Continue Shopping"<br>2. Observar la página resultante |
| **Resultado esperado** | El usuario regresa a la página de inventario |
| **Prioridad** | Baja |

### TC-16 - Ir al checkout desde el carrito
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario tiene un producto agregado y está en la página del carrito |
| **Pasos** | 1. Hacer clic en el botón "Checkout"<br>2. Observar la página resultante |
| **Resultado esperado** | Se abre la página de información del checkout |
| **Prioridad** | Alta |

## Módulo: Checkout

### TC-17 - Completar la información del comprador
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario está en el paso de información del checkout |
| **Datos** | Nombre, apellido y código postal válidos |
| **Pasos** | 1. Escribir el nombre en el campo "First Name"<br>2. Escribir el apellido en el campo "Last Name"<br>3. Escribir el código postal en el campo "Zip/Postal Code"<br>4. Hacer clic en el botón "Continue" |
| **Resultado esperado** | Se muestra el resumen de la compra (Overview) |
| **Prioridad** | Alta |

### TC-18 - Checkout con campos vacíos
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario está en el paso de información del checkout |
| **Pasos** | 1. Dejar los campos "First Name", "Last Name" y "Zip/Postal Code" vacíos<br>2. Hacer clic en el botón "Continue" |
| **Resultado esperado** | Se muestra el mensaje: *"Error: First Name is required"* |
| **Prioridad** | Media |

### TC-19 - Finalizar la compra
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario está en el resumen de la compra (Overview) |
| **Pasos** | 1. Revisar el resumen de la compra<br>2. Hacer clic en el botón "Finish" |
| **Resultado esperado** | Se muestra el mensaje de confirmación: *"Thank you for your order!"* |
| **Prioridad** | Alta |

### TC-20 - Cancelar el checkout
| Campo | Detalle |
|---|---|
| **Precondición** | El usuario está en el paso de información del checkout |
| **Pasos** | 1. Hacer clic en el botón "Cancel"<br>2. Observar la página resultante |
| **Resultado esperado** | El usuario regresa a la página del carrito |
| **Prioridad** | Baja |
