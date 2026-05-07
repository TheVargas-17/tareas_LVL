import flet as ft
from controllers.UserController import AuthController

def UserView(page, auth_controller):
    page.update()
    page.title = "Perfil"

    user = getattr(page, "user_data")

    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    telefono = ft.Text(f"Telefono: {user['telefono'] if user else 'Usuario'}", size=20)
    registro = ft.Text(f"Se registro el: {user['fecha_registro'] if user else 'Usuario'}", size=20)
    ultimo = ft.Text(f"Ultimo conectado: {user['ultimo_ingreso'] if user else 'Usuario'}", size=20)

    return ft.View(
        route="/perfil",
        controls=[

            ft.AppBar(
                title=ft.Text(f"Perfil de {user['nombre'] if user else 'Usuario'}", size=30),
                actions=[
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),

            ft.Container(
                padding=20,
                content=ft.Column(
                    [
                        ft.Divider(thickness=5, color=ft.Colors.BLUE),

                        apellido,
                        telefono,
                        registro,
                        ultimo
                    ],
                    spacing=10,
                    expand=True
                )
            ),
        ]
    )