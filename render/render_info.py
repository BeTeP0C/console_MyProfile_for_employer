from data.control_data import get_data_main, get_data_social, get_data_employer
from validate import PSAge, check_for_emptiness

def render_info_main (version = "default"):
  info = get_data_main(version)
  info_text = ""
  for key, value in info.items():
    if key == "name":
      value = str(check_for_emptiness(value))
      info_text += f'Имя: {value}\n'
    elif key == "age":
      value = str(check_for_emptiness(value))
      info_text += f"Возраст: {value} {PSAge(value)}\n"
    elif key == "phone":
      value = str(check_for_emptiness(value))
      info_text += f"Телефон: {value}\n"
    elif key == "mail":
      value = str(check_for_emptiness(value))
      info_text += f"E-mail: {value}\n"
    elif key == "index":
      value = str(check_for_emptiness(value))
      info_text += f"Индекс: {value}\n"
    elif key == "address":
      value = str(check_for_emptiness(value))
      info_text += f"Адрес: {value}\n"
    elif key == "add_info":
      value = str(check_for_emptiness(value))
      info_text += f"Дополнительная инофрмация: {value}"

  return info_text

def render_info_social ():
  info = get_data_social()
  info_text = ""
  for key, value in info.items():
    if key == "vk":
      value = str(check_for_emptiness(value))
      info_text += f'VK: {value}\n'
    elif key == "telegram":
      value = str(check_for_emptiness(value))
      info_text += f"Telegram: {value}\n"
    elif key == "tiktok":
      value = str(check_for_emptiness(value))
      info_text += f"TikTok: {value}\n"
    elif key == "youtube":
      value = str(check_for_emptiness(value))
      info_text += f"YouTube: {value}"

  return info_text

def render_info_employer():
  info = get_data_employer()
  info_text = ''
  for key, value in info.items():
    if key == "ogrnip":
      value = str(check_for_emptiness(value))
      info_text += f'ОГРНИП: {value}\n'
    elif key == "tin":
      value = str(check_for_emptiness(value))
      info_text += f"ИНН: {value}"

  return info_text

def render_info_bank ():
  info = get_data_employer()
  info_text = ''
  for key, value in info.items():
    if key == "checking_account":
      value = str(check_for_emptiness(value))
      info_text += f'Р/с: {value}\n'
    elif key == "bank":
      value = str(check_for_emptiness(value))
      info_text += f"Банк: {value}\n"
    elif key == "bic":
      value = str(check_for_emptiness(value))
      info_text += f"БИК: {value}\n"
    elif key == "correspondent_account":
      value = str(check_for_emptiness(value))
      info_text += f"К/с: {value}"
  return info_text

def render_fullinfo ():
  fullinfo = f'{render_info_main()}\n\n{render_info_social()}'
  return fullinfo

def render_fullinfo_business ():
  fullinfo = (
f'''{render_info_main("business")}

Информация о предпринимателе
{render_info_employer()}
Банковские реквизиты
{render_info_bank()}''')

  return fullinfo
