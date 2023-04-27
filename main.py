from render.render_menu_select_version import render_menu_select_version
from render.render_indent import render_indent
from render.render_start_message import render_start_message
from render.render_exit_program import render_exit_program
from versions.version_business import version_business
from versions.version_default import version_default

print(render_start_message())
print(render_indent())

while True:
  print(render_menu_select_version())
  version = int(input("Введите номер пункта меню: "))

  if version == 1:
    version_default()

  elif version == 2:
    version_business()
  elif not(version):
    print(render_exit_program())
    break
