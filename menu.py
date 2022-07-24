from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        # add widgets to window
        self.window.cols = 1
        self.window.add_widget(Image(source="logo.png"))
        self.add_or_gen = Label(
            text='Save a password?  Retrieve a password? Or Generate one?')
        self.window.add_widget(self.add_or_gen)
        self.save = Button(
            text='Save',
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FF00'
        )
        self.generate = Button(
            text='Generate',
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#FF06C1'
        )
        self.retrieve = Button(
            text='Generate',
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#06C1FF'
        )
        self.back = Button(
            pos_hint=(10, 10),
            text='Back',
            size=(100, 100),
            bold=True,
            background_color='#06C0FF'
        )

        self.window.add_widget(self.save)
        self.save.bind(on_press=self.save_new_pw)
        self.window.add_widget(self.generate)
        self.window.add_widget(self.retrieve)
        self.window.add_widget(self.back)

        return self.window

    def save_new_pw(self, button):
        self.url = TextInput(
            size_hint=(0.5, 0.5),
            hint_text='Please Enter the URL'
        )
        self.password = TextInput(
            size_hint=(0.5, 0.5),
            hint_text='Please Enter New Password'
        )
        self.username = TextInput(
            size_hint=(0.5, 0.5),
            hint_text='Please Enter Username if applicable'
        )
        self.email = TextInput(
            size_hint=(0.5, 0.5),
            hint_text='Please Enter Email if applicable'
        )
        self.app_name = TextInput(
            size_hint=(0.5, 0.5),
            hint_text='Please Enter Application Name'
        )
        self.window.add_widget(self.url)
        self.window.add_widget(self.password)
        self.window.add_widget(self.username)
        self.window.add_widget(self.email)
        self.window.add_widget(self.app_name)
        self.window.remove_widget(self.generate)
        self.window.remove_widget(self.retrieve)

    def gen_new_pw(self):
        pass


if __name__ == "__main__":
    SayHello().run()
