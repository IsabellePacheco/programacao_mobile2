import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    #criando um campo de texto
    campo_nome = ft.TextField(
        label='Digite seu nome'  , #texto que aparece acima do campo
        width=300, #largura do campo
        border_color=ft.Colors.PINK, #cor da borda
    )

    #texto que mostrara a resposta 
    resposta = ft.Text(
        value="", #inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER,
       
    )

    def processar_nome(evento):
        """
        funcap que pega o texto digitado pelo usuario e faz algo com ele
        """

        #pegando o valor digitado 
        nome_digitado = campo_nome.value

        #verificando se o usuario realmente digitou algo
        if nome_digitado== "" or nome_digitado is None:
            resposta.value = "Por favor, digite seu nome."
            resposta.color = ft.Colors.RED_300
        elif len(nome_digitado) < 2:
            resposta.value = "nome muito curto!"
            resposta.color = ft.Colors.ORANGE_300
        else:
            resposta.value = f"Olá, {nome_digitado}! Seja bem-vindo! " 
            resposta.color = ft.Colors.BLUE_300
            
        
        #atualize a interface 
        page.update()

    #botao para preocessar o nome
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150,
        bgcolor=ft.Colors.PINK_300, #cor de fundo
        color=ft.Colors.WHITE#cor do texto
    )

    #adicionar elementos a pagina 
    page.add(
        ft.Text("Digite seu nome abaixo:", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)


