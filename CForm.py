import dearpygui.dearpygui as dpg

dpg.create_context()

username = "admin"
password = "12345"

local_username = ""
local_password = ""

window_width = 960
window_height = 560

list_jawaban=[]
list_soal=[]

question = ""
dpg.create_viewport(title="CForm",decorated=False)
dpg.configure_viewport(0, x_pos=0, y_pos=0, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

def submit_username(sender):
    global local_username
    local_username = dpg.get_value(sender)

def submit_password(sender):
    global local_password
    local_password = dpg.get_value(sender)

def get_question(sender):
    global question
    question = dpg.get_value(sender)

def check_validation():
    if username == local_username and password == local_password:
        dpg.configure_item("main_menu",show=False)
        dpg.configure_item("panel_admin",show=True)
        dpg.set_primary_window(panel_admin,value=True)

def return_to_main_menu():
    dpg.configure_item("panel_admin",show=False)
    dpg.configure_item("main_menu",show=True)
    dpg.set_primary_window(main_menu_screen,value=True)

def add_question():
    print(question)
    dpg.add_text(question,parent="list",tag="quest")
    dpg.configure_item("text",default_value="")

with dpg.font_registry():
    font_sklscr = dpg.add_font(file="Font/slkscr.ttf",size=50)

with dpg.window(label="add_question",no_title_bar=True,no_close=True,show=False,modal=True,no_resize=True,tag='question',width=300,height=100):
    label = dpg.add_text("QUESTION")
    text_quest = dpg.add_input_text(callback=get_question)
    with dpg.group(horizontal=True):
        dpg.add_button(label="ADD",callback=add_question)
        dpg.add_button(label="BACK",callback=lambda:dpg.configure_item("question",show=False))

with dpg.window(label="admin_panel",no_title_bar=True,no_close=True,show=False,tag="panel_admin",no_resize=True) as panel_admin:
    child_window = dpg.add_child_window(width=880,height=330,show=True,tag='list')
    dpg.add_text("Hello",parent="list")
    with dpg.group(horizontal=True):
        add_btn = dpg.add_button(label="ADD",callback=lambda:dpg.configure_item("question",show=True))
        delete_btn = dpg.add_button(label="DELETE")
        back_btn = dpg.add_button(label="BACK",callback=return_to_main_menu)
        export_btn = dpg.add_button(label="EXPORT")

with dpg.windww(label="user_panel",no_title_bar=True,no_close=True,show=False,tag="user_panel_window",no_resize=True) as user_panel:
    


with dpg.window(label="Admin Login Panel",no_title_bar=True,no_close=True,modal=True,show=False,no_resize=True,tag="login_admin",width=300,height=150):
    username_label = dpg.add_text("USERNAME")
    username_input = dpg.add_input_text(tag="username",default_value="",callback=submit_username)
    password_label = dpg.add_text("PASSWORD")
    password_text = dpg.add_input_text(password=True,tag="password",default_value="",callback=submit_password)
    dpg.add_separator()

    with dpg.group(horizontal=True):
        dpg.add_spacer(width=50,height=15)
        dpg.add_button(label="LOGIN",callback=check_validation)
        dpg.add_button(label="BACK",callback=lambda:dpg.configure_item("login_admin",show=False))

with dpg.window(autosize=False, no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True,tag="main_menu") as main_menu_screen:

    dpg.add_spacer(height=350)
    admin = dpg.add_button(label="ADMIN",pos=[10,window_height-50],callback=lambda: dpg.configure_item("login_admin",show=True))
    user = dpg.add_button(label='USER',pos=[10,window_height-25])

    with dpg.group(horizontal=True):
        main_title = dpg.add_text(default_value="CFROM",pos=[window_width/2-100,window_height/2-50])
        dpg.bind_item_font(main_title,font_sklscr)


dpg.set_primary_window(window=main_menu_screen, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
