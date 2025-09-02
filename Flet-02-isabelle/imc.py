import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.PURPLE_200

    peso = ft.TextField(label="Peso (kg)", width=250, keyboard_type=ft.KeyboardType.NUMBER, color=ft.Colors.BLACK, bgcolor=ft.Colors.GREY_200, border_color=ft.Colors.GREY_500)
    altura = ft.TextField(label="Altura (m)", width=250, keyboard_type=ft.KeyboardType.NUMBER, color=ft.Colors.BLACK, bgcolor=ft.Colors.GREY_200, border_color=ft.Colors.GREY_500)

    resultado = ft.Text(
        value="Seu resultado aparecerá aqui",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.PURPLE_500
    )

    def calcular_imc(e):
        try:
            p: float = float(peso.value.replace(",", "."))
            a: float = float(altura.value.replace(",", "."))
            imc: float = p / (a ** 2)

            if imc < 18.5:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está abaixo do peso."
                resultado.color = ft.Colors.YELLOW_500
            elif 18.5 <= imc < 24.9:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com peso normal."
                resultado.color = ft.Colors.GREEN_500
            elif 25 <= imc < 29.9:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com sobrepeso."
                resultado.color = ft.Colors.ORANGE_500
            else:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com obesidade."
                resultado.color = ft.Colors.RED_500
        except ValueError:
            resultado.value = "Por favor, insira valores válidos."
            resultado.color = ft.Colors.WHITE

        page.update()

    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = "Seu resultado aparecerá aqui"
        resultado.color = ft.Colors.WHITE if page.bgcolor == ft.Colors.PURPLE else ft.Colors.WHITE
 
        page.update()

    # Função para alternar tema
    def alternar_tema(e):
        if page.bgcolor == ft.Colors.PURPLE_500:
            page.bgcolor = ft.Colors.PURPLE_200
            resultado.color = ft.Colors.PURPLE_500
            tema_btn.text = "Tema Claro"
        else:
            page.bgcolor = ft.Colors.PURPLE_500
            resultado.color = ft.Colors.PURPLE_200
            tema_btn.text = "Tema Escuro"
            
        page.update()

    tema_btn = ft.Switch( on_change=alternar_tema)

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        tema_btn
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),

                ft.Text("Calculadora de IMC", size=30, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                peso,
                altura,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Calcular", on_click=calcular_imc, bgcolor=ft.Colors.PURPLE_300, color=ft.Colors.PURPLE_100),
                        ft.ElevatedButton("Limpar", on_click=limpar, bgcolor=ft.Colors.PURPLE_300, color=ft.Colors.PURPLE_100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)