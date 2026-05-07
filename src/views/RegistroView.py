import flet as ft
from datetime import datetime

def RegistroView(page: ft.Page, auth_controller):
    
    def ver_contra(e):
        contrasena.password = not contrasena.password
        page.update()
        
    nombre = ft.TextField(
        label="Nombre",
        width=135,
        prefix_icon=ft.Icons.BADGE
    )

    apellido = ft.TextField(
        label="Apellido",
        width=135
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=280,
        prefix_icon=ft.Icons.CALL
    )

    correo = ft.TextField(
        label="Correo",
        width=280,
        prefix_icon=ft.Icons.PERSON
    )

    contrasena = ft.TextField(
        label="Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    def registra(e):
        if not nombre.value or not apellido.value or not correo.value or not contrasena.value or not telefono.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"))
            page.snack_bar.open = True
            page.update()
            return
        
        fecha = datetime.now().strftime("%Y-%m-%d")

        user, msg = auth_controller.registrar_Usuario(
            nombre.value,
            apellido.value,
            correo.value,
            contrasena.value,
            telefono.value,
            fecha
        )

        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

        if user:
            page.go("/")

    registrar = ft.ElevatedButton(
        "Registrarse",
        width=280,
        on_click=registra
    )

    def regresar(e):
        page.go("/")

    reversa = ft.TextButton(
        "Volver al login",
        on_click=regresar
    )

    contenido = ft.Container(
        content=ft.Column(
            [
                ft.Text("Crear cuenta", size=22, weight="bold"),
                
                ft.Row(
                    [nombre, apellido],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
                telefono,
                correo,
                contrasena,
                registrar,
                reversa
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=25,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        width=320
    )

    return ft.View(
        route="/registro",
        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white",
            center_title=True
        ),
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[contenido]
    )