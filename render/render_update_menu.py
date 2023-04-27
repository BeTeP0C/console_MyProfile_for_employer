def render_update_menu (version):
  return (
f'''ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ
1 - {"Общая" if version == "default" else version == "business" and "Личная"} информация
2 - {"Социальные сети и мессенджеры" if version == "default" else version == "business" and "Информация о предпринимателе"}
0 - Назад''')
