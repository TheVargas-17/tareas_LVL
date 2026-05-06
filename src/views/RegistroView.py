import flet as ft
from datetime import datetime

def RegistroView(page: ft.Page, auth_controller):
    
    def ver_contra(e):
        contraseña.password = not contraseña.password
        contraseña.update()
        
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

    contraseña = ft.TextField(
        label="Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    file_picker = ft.FilePicker()

    boton = ft.ElevatedButton(
        "Seleccionar imagen",
        width=280,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=[".jpg", ".jpeg", ".png"]
        )
    )
    
    def registra(e):
        if not correo.value and not contraseña.value and not nombre.value and not apellido.value and not telefono.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
        hoy = datetime.now()
        fecha = hoy.strftime("%Y-%m-%d")
        
        user, msg = auth_controller.registrar_Usuario(
            nombre.value, apellido.value, correo.value, contraseña.value, telefono.value, fecha
        )
        
        if user:
            page.go("/")
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
    
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
                contraseña,
                boton,
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
        controls=[
            contenido
        ]
    )