import flet as ft

def RegisterView(page, auth_controller):
    nombre = ft.TextField(label="Nombre", width=350)
    email = ft.TextField(label="Correo", width=350)
    password = ft.TextField(label="Contraseña", password=True, width=350)

    def registrar_click(e):
        success, msg = auth_controller.registrar_usuario(
            nombre.value,
            email.value,
            password.value
        )

        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True

        if success:
            page.go("/")  # regresar al login

        page.update()

    return ft.View(
        "/registro",
        [
            ft.AppBar(title=ft.Text("Registro")),
            ft.Column(
                [
                    ft.Text("Crear Cuenta", size=24, weight="bold"),
                    nombre,
                    email,
                    password,
                    ft.ElevatedButton("Registrarse", on_click=registrar_click),
                    ft.TextButton("Volver al login", on_click=lambda _: page.go("/"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )