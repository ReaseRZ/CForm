import dearpygui.dearpygui as dpg
from openpyxl import Workbook

dpg.create_context()

username = "admin"
password = "12345"

window_width = 960
window_height = 560
question_list = []

question = ""
dpg.create_viewport(title="CForm",decorated=False)
dpg.configure_viewport(0, x_pos=100, y_pos=100, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

workbook = Workbook()
worksheet = workbook.active

def get_question(sender):
    global question
    question = dpg.get_value(sender)

def check_validation():
    local_username = dpg.get_value("username")
    local_password = dpg.get_value("password")
    if username == local_username and password == local_password:
        dpg.configure_item("main_menu",show=False)
        dpg.configure_item("panel_admin",show=True)
        dpg.set_primary_window(panel_admin,value=True)

def return_to_main_menu():
    dpg.configure_item("panel_admin",show=False)
    dpg.configure_item("main_menu",show=True)
    dpg.set_primary_window(main_menu_screen,value=True)

def add_question():
    dpg.add_text(question,parent="user_child")
    ttl = dpg.add_input_text(parent="user_child",tag=f"user{len(question_list)}")
    dpg.add_separator(parent="user_child")
    quest_btn = dpg.add_text(question,parent="list",tag=f"quest{dpg.generate_uuid()}")
    dpg.configure_item("text",default_value="")
    question_list.append(f"user{len(question_list)}")

def submit_answer():
    container=[]
    for string in question_list:
        container.append(dpg.get_value(string))
        dpg.configure_item(string,default_value="")
    worksheet.append(container)

def open_user_panel():
    dpg.configure_item("main_menu",show=False)
    dpg.configure_item("user_panel_window",show=True)
    dpg.set_primary_window(user_panel,value=True)

def return_to_main_menu_from_user():
    dpg.configure_item("user_panel_window",show=False)
    dpg.configure_item("main_menu",show=True)

def export_data():
    dpg.configure_item("export_confirm",show=False)
    workbook.save("data.xlsx")

with dpg.font_registry():
    font_sklscr = dpg.add_font(file="Font/slkscr.ttf",size=50)

with dpg.window(label="add_question",no_title_bar=True,no_close=True,show=False,modal=True,no_resize=True,tag='question',width=300,height=100):
    label = dpg.add_text("QUESTION")
    text_quest = dpg.add_input_text(callback=get_question,tag="text")
    with dpg.group(horizontal=True):
        dpg.add_button(label="ADD",callback=add_question)
        dpg.add_button(label="BACK",callback=lambda:dpg.configure_item("question",show=False))

with dpg.window(label="admin_panel",no_title_bar=True,no_close=True,show=False,tag="panel_admin",no_resize=True) as panel_admin:
    child_window = dpg.add_child_window(width=880,height=400,show=True,tag='list')
    with dpg.group(horizontal=True):
        add_btn = dpg.add_button(label="ADD",callback=lambda:dpg.configure_item("question",show=True))
        #delete_btn = dpg.add_button(label="DELETE")
        back_btn = dpg.add_button(label="BACK",callback=return_to_main_menu)
        export_btn = dpg.add_button(label="EXPORT",callback=lambda:dpg.configure_item("export_confirm",show=True))

with dpg.window(label="user_panel",no_title_bar=True,no_close=True,show=False,tag="user_panel_window",no_resize=True) as user_panel:
    child = dpg.add_child_window(width=900,height=400,show=True,tag="user_child")
    dpg.add_spacer(width=300)
    submit_btn = dpg.add_button(label="SUBMIT",callback=submit_answer)
    back = dpg.add_button(label="BACK",callback=return_to_main_menu_from_user)

with dpg.window(label="export_confirmation",no_title_bar=True,no_close=True,modal=True,show=False,no_resize=True,tag="export_confirm",width=500,height=40):
    dpg.add_text("Are you sure want to export current data to excel ?")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=190)
        dpg.add_button(label="YES",callback=export_data)
        dpg.add_button(label="NO",callback=lambda:dpg.configure_item("export_confirm",show=False))

with dpg.window(label="Admin Login Panel",no_title_bar=True,no_close=True,modal=True,show=False,no_resize=True,tag="login_admin",width=300,height=150):
    username_label = dpg.add_text("USERNAME")
    username_input = dpg.add_input_text(tag="username",default_value="")
    password_label = dpg.add_text("PASSWORD")
    password_text = dpg.add_input_text(password=True,tag="password",default_value="")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=50,height=15)
        dpg.add_button(label="LOGIN",callback=check_validation)
        dpg.add_button(label="BACK",callback=lambda:dpg.configure_item("login_admin",show=False))

with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True,tag="main_menu") as main_menu_screen:


    dpg.add_spacer(height=350)
    admin = dpg.add_button(label="ADMIN",pos=[10,window_height-50],callback=lambda: dpg.configure_item("login_admin",show=True))
    user = dpg.add_button(label='USER',pos=[10,window_height-25],callback=open_user_panel)

    with dpg.group(horizontal=True):
        main_title = dpg.add_text(default_value="CFORM",pos=[window_width/2-100,window_height/2-50])
        dpg.bind_item_font(main_title,font_sklscr)


dpg.set_primary_window(window=main_menu_screen, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
