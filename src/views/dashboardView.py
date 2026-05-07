import flet as ft
from models.UsersModel import UsuarioModel

def DashboardView(page, tarea_controller):
    page.title = "Tareas"
    user = getattr(page, "user_data")

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    #  ELIMINAR 
    def eliminar(id_tarea):
        success, msg = tarea_controller.eliminar_tarea(id_tarea)

        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

        if success:
            refresh()

    #  REFRESH 
    def refresh():
        lista_tareas.controls.clear()

        if user and "id_usuario" in user:
            tareas = tarea_controller.obtener_lista(user["id_usuario"])

            for t in tareas:
                lista_tareas.controls.append(
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, ft.Colors.GREY),
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(t["titulo"], weight="bold"),
                                        ft.Text(t["descripcion"]),
                                        ft.Text(f"Estado: {t.get('estado','pendiente')}")
                                    ],
                                    expand=True
                                ),

                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color="red",
                                    on_click=lambda e, id=t["id_tarea"]: eliminar(id)
                                )
                            ]
                        )
                    )
                )

        page.update()

    refresh()

    #  CAMPOS 
    txt_titulo = ft.TextField(label="Tarea", expand=True)
    descripcion = ft.TextField(label="Descripción", expand=True)

    prioridad = ft.Dropdown(
        label="Prioridad",
        value="media",
        options=[
            ft.dropdown.Option("alta"),
            ft.dropdown.Option("media"),
            ft.dropdown.Option("baja"),
        ]
    )

    estado = ft.Dropdown(
        label="Estado",
        value="Pendiente",
        options=[
            ft.dropdown.Option("Pendiente"),
            ft.dropdown.Option("Terminada"),
        ]
    )

    #  AGREGAR 
    def add_task(e):
        if user and "id_usuario" in user:

            success, msg = tarea_controller.guardar_nueva(
                user["id_usuario"],
                txt_titulo.value,
                descripcion.value,
                prioridad.value,
                "General",
                estado.value,
            )

            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()

            if success:
                txt_titulo.value = ""
                descripcion.value = ""
                refresh()

    #  LOGOUT 
    def cerrar_sesion(e):
        UsuarioModel().cerrar_sesion(user["id_usuario"])
        page.go("/")

    
    return ft.View(
        route="/dashboard",
        controls=[

            ft.AppBar(
                title=ft.Text(f"Tareas de {user['nombre']}"),
                actions=[
                    ft.IconButton(ft.Icons.PERSON, on_click=lambda _: page.go("/perfil")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=cerrar_sesion)
                ],
            ),

            ft.Container(
                padding=20,
                content=ft.Column(
                    [

                        ft.Text("Nueva tarea", size=20, weight="bold"),

                        txt_titulo,
                        descripcion,

                        ft.Row([prioridad, estado]),

                        ft.ElevatedButton(
                            "Agregar tarea",
                            on_click=add_task
                        ),

                        ft.Divider(),

                        ft.Text("Mis tareas", size=18, weight="bold"),

                        lista_tareas
                    ]
                )
            )
        ]
    )