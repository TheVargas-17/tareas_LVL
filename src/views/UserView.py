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

    modificar_btn = ft.ElevatedButton("Modificar Perfil", on_click=lambda _: page.go("/modificar"))
    

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Nombre del usuario: {user['nombre'] if user else 'Usuario'}", size=40),
                
                actions=[
                    modificar_btn,
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                        ft.Divider(thickness=8,          
                                    color=ft.Colors.BLUE,
                                    ),
                        ft.Row([apellido]),
                        ft.Row([telefono]),
                        ft.Row([registro]),
                        ft.Row([ultimo])
                        
                ], expand=True),
                padding=20,expand=True
            ),
        ]
    )


def ModificarView(page, user):

    #  GUARDAR 
    def guardar_cambios(e):

        if not nombre_nuevo.value or not apellido_nuevo.value or not telefono_nuevo.value:
            page.snack_bar = ft.SnackBar(ft.Text("Complete los campos"))
            page.snack_bar.open = True
            page.update()
            return

        success = AuthController().modificar(
            user["id_usuario"],
            nombre_nuevo.value,
            apellido_nuevo.value,
            telefono_nuevo.value,
        )

        if success:
            user["nombre"] = nombre_nuevo.value
            user["apellido"] = apellido_nuevo.value
            user["telefono"] = telefono_nuevo.value

            page.user_data = user

            page.snack_bar = ft.SnackBar(ft.Text("Perfil actualizado"))
            page.snack_bar.open = True
            page.update()

            page.go("/perfil")

        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar"))
            page.snack_bar.open = True
            page.update()

    #  CAMPOS 
    nombre_nuevo = ft.TextField(label="Nombre")
    apellido_nuevo = ft.TextField(label="Apellido")
    telefono_nuevo = ft.TextField(label="Teléfono")

    #  BOTONES 
    guardar_btn = ft.ElevatedButton("Guardar cambios", on_click=guardar_cambios)
    salir_btn = ft.TextButton("Cancelar", on_click=lambda _: page.go("/perfil"))

    #  VIEW 
    return ft.View(
        route="/modificar",
        controls=[

            ft.Container(
                padding=20,
                content=ft.Column(
                    [

                        ft.Icon(ft.Icons.PERSON, size=60, color=ft.Colors.BLUE),

                        ft.Text("Editar perfil", size=22, weight="bold"),

                        nombre_nuevo,
                        apellido_nuevo,
                        telefono_nuevo,

                        ft.Row(
                            [guardar_btn, salir_btn],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ]
    )