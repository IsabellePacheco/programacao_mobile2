import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão "
    page.padding = 20

    #criando um texto que sera modificado pelo botao 
    mensagem = ft.Text(
        value="Clique no botão abaixo!", 
        size=20, 
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.PINK    )

    def botao_clicado(evento):
        """
        Sera executada quando o botao for clicado
        o prametro 'evento' contem informacoes sobre o evento de clique
        """

        #mudando o texto da mensagem
        mensagem.value = "Parabéns você clicou no botão!"
        mensagem.color = ft.Colors.BLUE_300

        #importante: sempre que modificamos elementos da interface, precisamos chamar page.update() para que as mudanças aparecam na tela 

        page.update()

    #criando um botao
    meu_botao = ft.ElevatedButton(
        text="Clique aqui!", #texto do botao
        on_click=botao_clicado, #função que sera chamada quando o botao for clicado
        width=200, #largura botao
        height=50, #altura botao
        bgcolor=ft.Colors.PINK_300, #cor de fundo
        color=ft.Colors.WHITE#cor do texto  
    )

    #adicionando elementos a pagina
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)