import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import flet as ft
from controllers.UserController import AuthController
from views.LoginView import LoginView
from views.RegisterView import RegisterView
from views.dashboard import DashboardView


def start(page: ft.Page):
    auth_ctrl = AuthController()

    page.title = "Sistema"
    page.window_width = 400
    page.window_height = 700

    # 🔥 FUNCIONES DE NAVEGACIÓN

    def ir_login():
        page.clean()
        page.add(LoginView(page, auth_ctrl, ir_dashboard, ir_registro))

    def ir_registro():
        page.clean()
        page.add(RegisterView(page, auth_ctrl, ir_login))

    def ir_dashboard():
        page.clean()
        page.add(DashboardView(page, ir_login))

    # 👇 INICIO
    ir_login()


ft.app(target=start)