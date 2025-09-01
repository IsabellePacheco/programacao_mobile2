import flet as ft

def main(page: ft.Page):
    page.title = "Contador completo"
    page.padding = ft.padding.only(top=40, left=20, bottom=20)

    valor_contador = 0

    #elementos da interface 
    display_contador = ft.Text(
        value="0",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
        text_align=ft.TextAlign.CENTER
    )

    info_contador = ft.Text(
        value="Contador iniciando em 0",
        size=14,
        color=ft.Colors.GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_display():
        """atualizar display e cor baseado no valor"""
        display_contador.value = str(valor_contador)
       
        if valor_contador > 0:
            display_contador.color = ft.Colors.GREEN
            info_contador.value = "Contador positivo"
        elif valor_contador < 0:
            display_contador.color = ft.Colors.RED
            info_contador.value = "Contador negativo"
        else:
            display_contador.color = ft.Colors.BLUE
            info_contador.value = "Contador zerado"

        page.update()
    
    def incrementar(e):
        nonlocal valor_contador
        valor_contador += 1
        atualizar_display()

    def decrementar(e):
        nonlocal valor_contador
        valor_contador -= 1
        atualizar_display()
    
    def resetar(e):
        nonlocal valor_contador
        valor_contador = 0
        atualizar_display()

    # botoes
    page.add(
        ft.Column(
            controls=[
                ft.Text("Contador Completo", size=24, weight=ft.FontWeight.BOLD),
                display_contador,
                info_contador,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("-", on_click=decrementar, width=80, height=80, bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),

                        ft.ElevatedButton("+", on_click=incrementar, width=80, height=80, bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE),
                                          
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                ),

                ft.ElevatedButton("Resetar", on_click=resetar, width=120, height=50, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
            