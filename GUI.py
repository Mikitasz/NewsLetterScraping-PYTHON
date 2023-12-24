import dearpygui.dearpygui as dpg
class GUI:
    def __init__(self) -> None:
        pass




    def save_callback(self):
        print("Save Clicked")
    def dearpy(self):
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=1000, height=800)
        dpg.setup_dearpygui()

        with dpg.window(label="Make NewsLetter"):
            dpg.add_text("Hello world")
            dpg.add_button(label="Save", callback=self.save_callback)
            dpg.add_input_text(label="string")
            dpg.add_slider_float(label="float")

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()