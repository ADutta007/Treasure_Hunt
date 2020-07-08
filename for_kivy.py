MyKivyFile='''
#: import MDRaisedButton kivymd.uix.button.MDRaisedButton
#: import MDTextField kivymd.uix.textfield.MDTextField
#: import GridLayout kivymd.uix.gridlayout.GridLayout
#: import MapView kivy_garden.mapview.MapView
#: import storagepath plyer.storagepath
#: import vibrator plyer.vibrator

WindowManager:
    MainWindow:
    SecondWindow:
    ThirdWindow:
    forkivymd:

<MainWindow>:


    name: "main"


    GridLayout:

        padding:40
        cols:1

        GridLayout:
            orientation:"horizontal"
            padding:60
            cols:2

            MDLabel:
                text: "Password: "
                halign:"center"
                size_hint:(0.5,1)
                pos_hint:{'center_x':0.5,'center_y':0.5}
                theme_text_color:"Custom"
                text_color:(236/255.,98/255.,81/255.,1)

            MDTextField:
                hint_text:"Code"
                fill_color:(0,4,2,1)
                pos_hint:{'center_x':0.5,'center_y':20}
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                id: passw
                multiline: True
                password: True
                text_color:(236/255.,98/255.,81/255.,1)

        MDRaisedButton:
            text: "Submit"
            on_release:
                app.root.current = "second" if passw.text == "ashish" else "main"
                root.manager.transition.direction = "left"



<SecondWindow>:
    name: "second"

    GridLayout:
        cols:2
        Button:
            text:"MAP"
            on_release:
                app.root.current = "map"

        Button:
            text:"Functions"
            on_release:
                app.root.current="function"

<ThirdWindow>:
    name:"map"

    MapView:
        lat:27.6922368
        lon:85.3344256
        zoom:14
<forkivymd>:
    name:"function"
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        MDRaisedButton:
            text:"Vibrate"
            on_release:
                vibrator.pattern(0,4)
'''