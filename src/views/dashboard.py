import flet as ft

def DashboardView(page):

    # PROTEGER RUTA (si no hay sesión)
    user = page.session.get("user")

    if not user:
        page.go("/")
        return ft.View("/", [])  # evita errores

    #  FUNCIÓN LOGOUT
    def logout(e):
        page.session.clear()
        page.go("/")
        page.update()

    return ft.View(
        "/dashboard",
        [
            ft.AppBar(
                title=ft.Text(f"Bienvenido {user['nombre']}"),
                actions=[
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        tooltip="Cerrar sesión",
                        on_click=logout
                    )
                ]
            ),

            ft.Column(
                [
                    ft.Text("Estás dentro del sistema 🎉", size=20),
                    ft.Text(f"Correo: {user['email']}"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )