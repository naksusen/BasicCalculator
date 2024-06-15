import math

import flet as ft

def main(page: ft.page):
    page.title = "Calculator"
    page.window_height = 580
    page.window_width = 460
    page.bgcolor = "#ffc8ee"
    page.window_resizable = False
    txtcol = ft.Column()
    displaycol = ft.Column(scroll=ft.ScrollMode.AUTO)

    ft.Text("Size 10", size=10),
    txt = ft.TextField(
        label="Calculator",
        border=ft.InputBorder.NONE,
        cursor_color=ft.colors.PINK_200,
        bgcolor='#dbe7ea',
        color='#6e4229',
        filled=True,
        focused_bgcolor='#dbe7ea',
        border_radius=20,
        border_color='#5b2914',
        focused_border_color='#6e4229',
        prefix_icon=ft.icons.CALCULATE_ROUNDED,
        text_style=ft.TextStyle(size=30, color="#6e4229",),
        disabled=True,
    )
    #page.add(txt)
    txtcol.controls.append(txt)

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

    btnc = ft.ElevatedButton(
        text="C", bgcolor="#FFC90E", color="#6e4229", data="c", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=40))
    )
    btndel = ft.ElevatedButton(
        text="<", bgcolor="#bfe8fc", color="#6e4229", data="e", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnopen = ft.ElevatedButton(
        text="(", bgcolor="#bfe8fc", color="#6e4229", data="(", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnclose = ft.ElevatedButton(
        text=")", bgcolor="#bfe8fc", color="#6e4229", data=")", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )

    r1 =ft.Row(
        controls=[btnc,btndel,btnopen, btnclose],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    #page.add(r1)
    displaycol.controls.append(r1)

    btnsqrt = ft.ElevatedButton(
        text="√", bgcolor="#bfe8fc", color="#6e4229", data="√", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btncos = ft.ElevatedButton(
        text="cos0", bgcolor="#bfe8fc", color="#6e4229", data="cos0", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btntan = ft.ElevatedButton(
        text="tan0", bgcolor="#bfe8fc", color="#6e4229", data="tan0", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnsin = ft.ElevatedButton(
        text="sin0", bgcolor="#bfe8fc", color="#6e4229", data="sin0", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    r6 = ft.Row(
        controls=[btncos, btntan, btnsin, btnsqrt],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    # page.add(r6)
    displaycol.controls.append(r6)

    btncosh = ft.ElevatedButton(
        text="cosh", bgcolor="#bfe8fc", color="#6e4229", data="cosh", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btntanh = ft.ElevatedButton(
        text="tanh", bgcolor="#bfe8fc", color="#6e4229", data="tanh", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnsinh = ft.ElevatedButton(
        text="sinh", bgcolor="#bfe8fc", color="#6e4229", data="sinh", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btndiv = ft.ElevatedButton(
        text="/", bgcolor="#bfe8fc", color="#6e4229", data="/", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    r7 = ft.Row(
        controls=[btncosh, btntanh, btnsinh, btndiv],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    # page.add(r7)
    displaycol.controls.append(r7)

    btn7 = ft.ElevatedButton(
        text="7", bgcolor="#bfe8fc", color="#6e4229", data="7", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn8 = ft.ElevatedButton(
        text="8", bgcolor="#bfe8fc", color="#6e4229", data="8", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn9 = ft.ElevatedButton(
        text="9", bgcolor="#bfe8fc", color="#6e4229", data="9", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnmulti = ft.ElevatedButton(
        text="*", bgcolor="#bfe8fc", color="#6e4229", data="*", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )


    r2 = ft.Row(
        controls=[btn7, btn8, btn9, btnmulti],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    #page.add(r2)
    displaycol.controls.append(r2)

    btn4 = ft.ElevatedButton(
        text="4", bgcolor="#bfe8fc", color="#6e4229", data="4", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn5 = ft.ElevatedButton(
        text="5", bgcolor="#bfe8fc", color="#6e4229", data="5", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn6 = ft.ElevatedButton(
        text="6", bgcolor="#bfe8fc", color="#6e4229", data="6", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnsub = ft.ElevatedButton(
        text="-", bgcolor="#bfe8fc", color="#6e4229", data="-", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )

    r3 = ft.Row(
        controls=[btn4, btn5, btn6, btnsub],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    #page.add(r3)
    displaycol.controls.append(r3)

    btn1 = ft.ElevatedButton(
        text="1", bgcolor="#bfe8fc", color="#6e4229", data="1", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn2 = ft.ElevatedButton(
        text="2", bgcolor="#bfe8fc", color="#6e4229", data="2", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btn3 = ft.ElevatedButton(
        text="3", bgcolor="#bfe8fc", color="#6e4229", data="3", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btnadd = ft.ElevatedButton(
        text="+", bgcolor="#bfe8fc", color="#6e4229", data="+", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )


    r4 = ft.Row(
        controls=[btn1, btn2, btn3, btnadd],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    #page.add(r4)
    displaycol.controls.append(r4)


    btn0 = ft.ElevatedButton(
        text="0", bgcolor="#bfe8fc", color="#6e4229", data="0", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btndot = ft.ElevatedButton(
        text=".", bgcolor="#bfe8fc", color="#6e4229", data=".", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btneq = ft.ElevatedButton(
        text="=", bgcolor="#FFC90E", color="#6e4229", data="=", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    btns2 = ft.ElevatedButton(
            text="x\u00B2", bgcolor="#bfe8fc", color="#6e4229", data="x\u00B2", on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=60))
    )
    r5 = ft.Row(
        controls=[btn0, btndot, btns2, btneq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN.SPACE_EVENLY
    )
    #page.add(r5)
    displaycol.controls.append(r5)


    displaycon = ft.Container(
        ft.Column(
            [txtcol, displaycol], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PINK_200],
        ),

        expand=False,
        width=500,
        height=550,
        margin=10,
        padding=29,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )
    page.add(displaycon)


ft.app(target=main)