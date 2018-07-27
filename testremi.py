import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width = 120, height = 100)
        self.lbl = gui.Label('Temperature')
        self.lbl2 = gui.Label('Humidity')
        self.bt = gui.Button('Click to Refresh')

        # setting the listener for the onclick event of the button
        self.bt.onclick.connect(self.on_button_pressed)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.lbl2)
        container.append(self.bt)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('Click to Refresh!')
        self.bt.set_text('Click to Refresh')

# starts the webserver
start(MyApp,address='192.168.1.28',port=8081)