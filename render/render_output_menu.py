def render_output_menu (version):
  return (
f'''ВЫВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ
1 - {"Общая" if version == "default" else version == "business" and "Личная"} информация
2 - Вся информация
0 - Назад''')
