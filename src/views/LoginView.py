import flet as ft

def LoginView(page, auth_controller, ir_dashboard, ir_registro):

    email_input = ft.TextField(
        label="Correo",
        width=280,
        prefix_icon=ft.Icons.EMAIL
    )

    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        prefix_icon=ft.Icons.LOCK
    )

    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Llena todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        user, msg = auth_controller.login(
            email_input.value,
            pass_input.value
        )

        if user:
            page.session.set("user", user)
            ir_dashboard()
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()

    return ft.Column(
        [
            ft.Container(height=40),

            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.LOCK_PERSON, size=60, color=ft.Colors.BLUE),
                        ft.Text("Bienvenido", size=26, weight="bold"),
                        ft.Text("Inicia sesión para continuar", size=14, color="grey"),
                        email_input,
                        pass_input,
                        ft.ElevatedButton(
                            "Entrar",
                            width=280,
                            height=45,
                            on_click=login_click
                        ),
                        ft.TextButton(
                            "Crear cuenta",
                            on_click=lambda e: ir_registro()
                        )
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=25,
                width=320,
                border_radius=15,
                bgcolor="white",
                shadow=ft.BoxShadow(blur_radius=15, color="black12")
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )