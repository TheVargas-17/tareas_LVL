import flet as ft
from views.RegistroView import RegistroView
from datetime import datetime


def LoginView(page: ft.Page, auth_controller):
    
    def ver_contra(e):
        contra.password = not contra.password
        contra.update()
        
    correo = ft.TextField(
    label="Correo",
    width=280,
    prefix_icon=ft.Icons.PERSON,
    color=ft.Colors.BLACK
)

    contra = ft.TextField(
    label="Contraseña",
    width=280,
    password=True,
    can_reveal_password=True,
    prefix_icon=ft.Icons.LOCK,
    color=ft.Colors.BLACK
)
    
    def login_click(e):
        if not correo.value or not contra.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
        user, msg = auth_controller.login(correo.value, contra.value)
    
        if user:
            page.user_data = user
            page.go("/dashboard")
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
            
    def olvidado(e):
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
    
    def registro(e):
        page.go("/registro")
    
    iniciar = ft.ElevatedButton(
        "Iniciar sesión",
        width=280,
        on_click=login_click
    )

    registrarse = ft.TextButton("Crear cuenta", on_click=registro)
    olvidada = ft.TextButton("¿Olvidaste tu contraseña?", on_click=olvidado)

    contenido = ft.Container(
        content=ft.Column(
            [
                ft.Text("Acceso", size=22, weight="bold"   , color=ft.Colors.BLACK
),
                correo,
                contra,
                iniciar,
                olvidada,
                registrarse
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
        route="/",
        appbar=ft.AppBar(
            title=ft.Text("Login"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white",
            center_title=True  
        ),
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            contenido
        ]
    )