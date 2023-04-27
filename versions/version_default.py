from data.control_data import get_data_main, get_data_social
from data.save_user_info import save_user_main_info, save_user_social_info
from render.render_indent import render_indent
from render.render_info import render_fullinfo, render_info_main
from render.render_main_menu import render_main_menu
from render.render_output_menu import render_output_menu
from render.render_update_menu import render_update_menu

def version_default ():
  version = "default"
  print(render_indent())
  print("Вы находитесь в обычной версии", end="\n\n")
  while True:
    print(render_main_menu())
    option_main = input("Введите номер пункта меню: ")

    if option_main == "1":
      print(render_indent())
      while True:
        print(render_update_menu(version))
        option = input("Введите номер пункта меню: ")

        if option == "1":
          main_info = get_data_main(version)
          save_user_main_info(main_info, version)
          print(render_indent())
        elif option == "2":
          social_info = get_data_social()
          save_user_social_info(social_info)
          print(render_indent())
        elif option == "0":
          print(render_indent(), end="\n\n")
          break
    elif option_main == "2":
      print(render_indent())
      while True:
        print(render_output_menu(version))
        option = input("Введите номер пункта меню: ")

        if option == "1":
          print(render_info_main(version))
          print(render_indent())
        elif option == "2":
          print(render_fullinfo())
          print(render_indent())
        elif option == "0":
          print(render_indent(), end="\n\n")
          break
    elif option_main == "0":
      print(render_indent(), end="\n\n")
      break
