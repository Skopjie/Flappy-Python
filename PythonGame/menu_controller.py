from button_controller import Button

class MenuController():
    def __init__(self):
        self.button_array = []
        self.is_actived = True

    def add_new_button(self, button):
        self.button_array.append(button)

    def draw(self):
        if self.is_actived:
            for button in self.button_array:
                button.draw()

    def handle_event(self, event):
        if self.is_actived:
            for button in self.button_array:
                button.handle_event(event)

    def set_active(self, new_is_actived):
        self.is_actived = new_is_actived
