import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Gerador de Senhas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 350
    page.window_height = 600
    page.padding = 20
    # page.bgcolor = "#E9F5E1"  # fundo neutro claro
    page.text_align="center"

    senha_atual = ""

    def gerar_senha(e):
        nonlocal senha_atual
        comprimento = int(slider.value)
        caracteres = ""
        if upper_switch.value:
            caracteres += string.ascii_uppercase
        if lower_switch.value:
            caracteres += string.ascii_lowercase
        if numbers_switch.value:
            caracteres += string.digits
        if symbols_switch.value:
            caracteres += string.punctuation

        if caracteres:
            senha = "".join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha
            senha_atual = senha
            copiar_btn.visible = True
        else:
            senha_output.value = "Selecione ao menos um tipo de caractere."
            senha_atual = ""
            copiar_btn.visible = False
        page.update()

    def mostrar_senha_copiada(e):
        if senha_atual:
            text_display.value = f"Senha copiada: {senha_atual}"
            text_display.visible = True
            page.update()
            try:
                page.set_clipboard(senha_atual)
            except:
                pass

    def togle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.DARK_MODE if is_dark else ft.Icons.LIGHT_MODE
        page.update()

    is_dark = False

    theme_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        on_click=togle_theme,
        icon_color="#556B2F"  # verde musgo
    )

    title_switch_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Gerador de Senhas", size=26, weight="bold", color="#556B2F", text_align="center"),
            theme_button
        ]
    )

    senha_output = ft.TextField(
        value="",
        label="Senha Gerada",
        read_only=True,
        width=280,
        bgcolor="#E9F5E1",  # verde bem suave
        border_color="#556B2F",
        color="#2F4F1F"
    )

    text_display = ft.Text(
        value="",
        color="#228B22",  # verde vibrante para feedback
        visible=False
        
    )

    copiar_btn = ft.ElevatedButton(
        text="COPIAR SENHA",
        on_click=mostrar_senha_copiada,
        color="white",
        bgcolor="#556B2F",
        visible=False
    )

    slider = ft.Slider(
        min=8,
        max=20,
        value=12,
        divisions=12,
        label="CARACTERES: {value}",
        active_color="#556B2F",
        thumb_color="#6B8E23",
    )

    upper_switch = ft.Switch(label="Letras maiúsculas", active_color="#556B2F")
    lower_switch = ft.Switch(label="Letras minúsculas", value=True, active_color="#556B2F")
    numbers_switch = ft.Switch(label="Incluir números", active_color="#556B2F")
    symbols_switch = ft.Switch(label="Incluir símbolos", active_color="#556B2F")

    preferencias_column = ft.Column(
        [
            ft.Text("PREFERÊNCIAS", size=16, weight="bold", color="#556B2F"),
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    gerar_button = ft.ElevatedButton(
        text="GERAR SENHA",
        on_click=gerar_senha,
        color="white",
        bgcolor="#6B8E23"
    )

    page.add(
        ft.Column(
            [
                title_switch_row,
                senha_output,
                text_display,
                copiar_btn,
                slider,
                preferencias_column,
                gerar_button,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )

ft.app(
    target=main,
    assets_dir="assets"
)
