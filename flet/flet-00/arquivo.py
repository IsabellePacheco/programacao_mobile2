
import flet as ft

def main(page: ft.Page):
    text_name = ft.TextField(label="Seu nome")
    def btn_click(e):
        page.add(ft.Text(f"Olá, {text_name.value}!"))
    page.add(text_name, ft.ElevatedButton("Diga Olá", on_click=btn_click))

ft.app(target=main)