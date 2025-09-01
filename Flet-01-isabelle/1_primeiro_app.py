import flet as ft

def main(page: ft.Page):
    """
    funcao principal que sera executada quando o app iniciar.
    o parametro 'page' representa a tela/pagina do nosso app.
    """

    #configurações básicas da página
    page.title = "Meu primeiro app Flet" #titulo que aparece na aba do navegador
    page.padding = 20 # espaçamentos interno da pagina 

    #criando nosso primeiro elemento:um texto
    meu_texto = ft.Text(
        value="Hello world!", #texto exibido
        size=24, #fonte
        color=ft.Colors.BLUE, #cor
        weight=ft.FontWeight.BOLD, #negrito
        text_align=ft.TextAlign.CENTER #alinhamento
    )

    #adicionar texto a pagina 
    page.add(meu_texto)

    #mais elementos 
    page.add(
        ft.Text(" Bem vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text(" ComFlet, você pode criar apps incríveis!", size=16, color=ft.Colors.GREEN)
    )

#esta linha inicia nosso aplicativo, chamando a funcao main
ft.app(target=main)
