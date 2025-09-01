import flet as ft

def main(page: ft.Page):
    page.title = "Layouts Basico"
    page.padding = 20

    #layout organizado utilizando column (vertical) e row (horizontal
    
    #titulo primncipal
    titulo = ft.Text(
        "Organizando Elementos na Tela", 
        size=24, 
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
        text_align=ft.TextAlign.CENTER
    )

    #criando uma linha horizoltal com 3 botoes
    linha_botoes = ft.Row(
        controls=[
            ft.ElevatedButton(text="Botao 1", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, width=100),
            ft.ElevatedButton(text="Botao 2", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, width=100),
            ft.ElevatedButton(text="Botao 3", bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE, width=100),
        ],
        alignment=ft.MainAxisAlignment.CENTER, #espaco entre os botoes
        spacing=20 #espaco entre os botoes
    )

    #criando caizas coloridas em colunas 
    caixa1 = ft.Container(
        content=ft.Text("Caixa 1", color=ft.Colors.WHITE,),
        bgcolor=ft.Colors.PURPLE,
        width=200,
        height=50,
        alignment=ft.alignment.center,
        border_radius=5
    )

    caixa2 = ft.Container(
        content=ft.Text("Caixa 2", color=ft.Colors.WHITE,),
        bgcolor=ft.Colors.ORANGE,
        width=200,
        height=50,
        alignment=ft.alignment.center,
        border_radius=5
    )

    #organizando as caixas em uma coluna
    coluna_caixas = ft.Column(
        controls=[caixa1, caixa2],
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    #layout principal organizado tudo verticalmente
    layout_principal = ft.Column(
        controls=[
            titulo, 
            ft.Text("Linha horizontal de botoes", size=16,),
            linha_botoes,
            ft.Text("Coluna de caixas coloridas", size=16,),
            coluna_caixas,
            ft.Text("Layout organizado!", size=14, color=ft.Colors.GREEN)
        ],
        
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25
    )

    #adicionando tudo a pagina 
    page.add(layout_principal)

ft.app(target=main)
