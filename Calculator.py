import math

import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.window_height = 580
    page.window_width = 460
    page.bgcolor = "#ffc8ee"
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # State variable to control which screen to show
    show_calculator = False

    def show_calculator_ui():
        txtcol = ft.Column()
        displaycol = ft.Column(scroll=ft.ScrollMode.AUTO)

        # Add a title at the top
        title = ft.Text(
            "Scientific Calculator",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#6e4229",
            text_align=ft.TextAlign.CENTER,
        )

        txt = ft.TextField(
            label="Calculator",
            border=ft.InputBorder.NONE,
            cursor_color=ft.colors.PINK_200,
            bgcolor=None,
            color='#6e4229',
            filled=True,
            focused_bgcolor=None,
            border_radius=20,
            border_color='#5b2914',
            focused_border_color='#6e4229',
            prefix_icon=ft.icons.CALCULATE_ROUNDED,
            text_style=ft.TextStyle(size=30, color="#6e4229",),
            disabled=True,
        )
        txt_container = ft.Container(
            txt,
            border_radius=20,
            padding=ft.padding.only(left=8, right=8, top=4, bottom=4),
            bgcolor="#dbe7ea",
            border=ft.border.all(2, ft.colors.with_opacity(0.15, ft.colors.BLACK)),
            gradient=None
        )
        txtcol.controls.append(txt_container)

        def keyboard(e):
            data = e.control.data
            if data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "/", "*", "(", ")"]:
                txt.value = str(txt.value) + str(data)
                page.update()
            elif data == "=":
                txt.value=str(eval(txt.value))
                page.update()
            elif data == "e":
                txt.value=txt.value[:-1]
                page.update()
            elif data=="c":
                txt.value=""
                page.update()
            elif data=="√":
                txt.value=str(math.sqrt(eval(txt.value)))
                page.update()
            elif data=="∛":
                txt.value=str(eval(txt.value) ** (1/3))
                page.update()
            elif data=="cos0":
                txt.value= str(math.cos(math.radians(eval(txt.value))))
                page.update()
            elif data=="tan0":
                txt.value= str(math.tan(math.radians(eval(txt.value))))
                page.update()
            elif data=="sin0":
                txt.value= str(math.sin(math.radians(eval(txt.value))))
                page.update()
            elif data == "cosh":
                txt.value = str(math.cosh(math.radians(eval(txt.value))))
                page.update()
            elif data == "tanh":
                txt.value = str(math.tanh(math.radians(eval(txt.value))))
                page.update()
            elif data == "sinh":
                txt.value = str(math.sinh(math.radians(eval(txt.value))))
                page.update()
            elif data=='x\u00B2':
                txt.value=str(eval(txt.value)**2)
                page.update()
            elif data == "^":
                txt.value = str(txt.value) + "**"
                page.update()
            elif data == "10^x":
                txt.value = str(10 ** eval(txt.value))
                page.update()
            elif data == "e^x":
                txt.value = str(math.exp(eval(txt.value)))
                page.update()
            elif data == "log":
                txt.value = str(math.log10(eval(txt.value)))
                page.update()
            elif data == "ln":
                txt.value = str(math.log(eval(txt.value)))
                page.update()
            elif data == "π":
                txt.value = str(txt.value) + str(math.pi)
                page.update()
            elif data == "e_const":
                txt.value = str(txt.value) + str(math.e)
                page.update()
            elif data == "sin⁻¹":
                txt.value = str(math.degrees(math.asin(eval(txt.value))))
                page.update()
            elif data == "cos⁻¹":
                txt.value = str(math.degrees(math.acos(eval(txt.value))))
                page.update()
            elif data == "tan⁻¹":
                txt.value = str(math.degrees(math.atan(eval(txt.value))))
                page.update()
            elif data == "!":
                txt.value = str(math.factorial(int(eval(txt.value))))
                page.update()
            elif data == "|x|":
                txt.value = str(abs(eval(txt.value)))
                page.update()
            elif data == "1/x":
                txt.value = str(1 / eval(txt.value))
                page.update()
            elif data == "%":
                txt.value = str(eval(txt.value) / 100)
                page.update()

        def create_button(text, data, bgcolor="#bfe8fc"):
            return ft.ElevatedButton(
                text=text,
                bgcolor=bgcolor,
                color="#6e4229",
                data=data,
                on_click=keyboard,
                style=ft.ButtonStyle(
                    shape=ft.ContinuousRectangleBorder(radius=60),
                    shadow_color=ft.colors.BLACK45,
                    elevation=8,
                    animation_duration=300,
                    overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                ),
            )

        # --- Scientific Calculator Layout ---
        # Top row: inv, pi, e, C, del
        r1 = ft.Row(
            controls=[
                create_button("1/x", "1/x"),
                create_button("π", "π"),
                create_button("e", "e_const"),
                create_button("C", "c", "#FFC90E"),
                create_button("<", "e")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.clear()
        displaycol.controls.append(r1)

        # Second row: x^y, x², √, ∛, %
        r2 = ft.Row(
            controls=[
                create_button("xʸ", "^"),
                create_button("x²", "x²"),
                create_button("√", "√"),
                create_button("∛", "∛"),
                create_button("%", "%")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r2)

        # Third row: ln, log, eˣ, 10ˣ, !
        r3 = ft.Row(
            controls=[
                create_button("ln", "ln"),
                create_button("log", "log"),
                create_button("eˣ", "e^x"),
                create_button("10ˣ", "10^x"),
                create_button("n!", "!")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r3)

        # Fourth row: sin, cos, tan, sin⁻¹, cos⁻¹, tan⁻¹
        r4 = ft.Row(
            controls=[
                create_button("sin", "sin0"),
                create_button("cos", "cos0"),
                create_button("tan", "tan0"),
                create_button("sin⁻¹", "sin⁻¹"),
                create_button("cos⁻¹", "cos⁻¹"),
                create_button("tan⁻¹", "tan⁻¹")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r4)

        # Fifth row: sinh, cosh, tanh, |x|, (, )
        r5 = ft.Row(
            controls=[
                create_button("sinh", "sinh"),
                create_button("cosh", "cosh"),
                create_button("tanh", "tanh"),
                create_button("|x|", "|x|"),
                create_button("(", "("),
                create_button(")", ")")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r5)

        # Number and operator rows (standard layout)
        r6 = ft.Row(
            controls=[
                create_button("7", "7"),
                create_button("8", "8"),
                create_button("9", "9"),
                create_button("/", "/")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r6)

        r7 = ft.Row(
            controls=[
                create_button("4", "4"),
                create_button("5", "5"),
                create_button("6", "6"),
                create_button("*", "*")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r7)

        r8 = ft.Row(
            controls=[
                create_button("1", "1"),
                create_button("2", "2"),
                create_button("3", "3"),
                create_button("-", "-")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r8)

        r9 = ft.Row(
            controls=[
                create_button("0", "0"),
                create_button(".", "."),
                create_button("=", "=", "#FFC90E"),
                create_button("+", "+")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
        )
        displaycol.controls.append(r9)

        displaycon = ft.Container(
            ft.Column(
                [title, txtcol, displaycol],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.PINK_200, ft.colors.PINK_100],
            ),
            expand=False,
            width=500,
            height=550,
            margin=10,
            padding=29,
            border_radius=20,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=25,
                color=ft.colors.BLACK45,
                offset=ft.Offset(5, 5),
            ),
            border=ft.border.all(2, ft.colors.with_opacity(0.1, ft.colors.WHITE))
        )
        page.controls.clear()
        page.add(displaycon)

    def start_click(e):
        nonlocal show_calculator
        show_calculator = True
        show_calculator_ui()
        page.update()

    if not show_calculator:
        # Show the start page
        engaging_text = ft.Text(
            "Ready to crunch numbers? Start your scientific journey!",
            size=26,
            weight=ft.FontWeight.BOLD,
            color="#d72660",
            text_align=ft.TextAlign.CENTER,
            italic=True,
        )
        start_btn = ft.ElevatedButton(
            text="Start",
            bgcolor="#FFC90E",
            color="#6e4229",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=40),
                padding=ft.padding.symmetric(horizontal=40, vertical=20),
                text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)
            ),
            width=220,
            height=60,
            on_click=start_click
        )
        start_col = ft.Column([
            engaging_text,
            ft.Container(height=40),
            start_btn
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        start_con = ft.Container(
            start_col,
            width=500,
            height=550,
            margin=10,
            padding=29,
            border_radius=20,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.PINK_200, ft.colors.PINK_100],
            ),
            border=ft.border.all(2, ft.colors.with_opacity(0.1, ft.colors.WHITE))
        )
        copyright_text = ft.Text(
            "© 2025 Janet. All rights reserved.",
            size=14,
            color="#6e4229",
            text_align=ft.TextAlign.CENTER,
            italic=True,
            opacity=0.7,
        )
        page.add(start_con)
        page.add(copyright_text)
    else:
        show_calculator_ui()

ft.app(target=main)