import flet as ft

def main(page: ft.Page):
    page.title = "seletor de cores "
    page.padding = 20

    #container que mudara de cor 
    caixa_colorida = ft.Container(
        content=ft.Text(
            "escolha uma Cor", 
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),

        width=300,
        height=100,
        bgcolor=ft.Colors.GREY,
        border_radius=10,
        alignment=ft.alignment.center       
    )

    def cor_selecionada(evento):
        """
        esta funcao é executada sempre que o usuario escolhe uma cor
        """
        #pegando qual cor foi selecionada
        cor_escolhida = evento.control.value

        #diionar com as cores disponiveis
        #é como uma "lista de correspondencia" entre nome e cor real
        cores_disponiveis = {
            "vermelho": ft.Colors.RED,
            "verde": ft.Colors.GREEN,
            "azul": ft.Colors.BLUE,
            "laranja": ft.Colors.ORANGE,
            "roxo": ft.Colors.PURPLE,
            "rosa": ft.Colors.PINK,       
        }

        #mudando a cor da caixa 
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"cor selecionada {cor_escolhida}"

        page.update()

    #criaando lista suspensa 
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("vermelho"),
            ft.dropdown.Option("verde"),
            ft.dropdown.Option("azul"),
            ft.dropdown.Option("laranja"),
            ft.dropdown.Option("roxo"),
            ft.dropdown.Option("rosa"),            
        ],
        on_change=cor_selecionada,
    )

    #adicionar elementos a pagina
    page.add(
        ft.Text("Selecione uma cor da lista abaixo:", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colorida
    )

ft.app(target=main)