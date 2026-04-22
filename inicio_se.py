import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario = ft.TextField(label="Usuario", width=250)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    mensaje = ft.Text()

    def login(e):
        if usuario.value == "admin" and password.value == "1234":
            mensaje.value = "Inicio de sesión correcto"
            mensaje.color = "green"
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
        page.update()

    boton_login = ft.ElevatedButton("Iniciar sesión", on_click=login)

    page.add(
        ft.Column(
            [
                ft.Text("Login", size=30),
                usuario,
                password,
                boton_login,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)