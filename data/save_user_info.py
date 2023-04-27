from data.control_data import update_data_main, update_data_social, update_data_employer
from validate import check_name, check_age, check_phone, check_mail, check_index, check_social, check_account, check_all_employer_point, check_ogrnip, check_tin, deleteLetters, check_bic

def save_user_main_info (main_info, version):
  for key in main_info:
    while True:
      if key == "name":
        answer = input("Как вас зовут: ")
        response = check_name(answer)

        if response["status"]:
          main_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "age":
        answer = input("Сколько вам лет: ")
        response = check_age(answer)

        if response["status"]:
          main_info[key] = int(answer)
          break
        else:
          print(response["message"])

      if key == "phone":
        answer = input("Введите свой номер телефона: ")
        response = check_phone(answer)

        if response["status"]:
          main_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "mail":
        answer = input("Введите вашу почту: ")
        response = check_mail(answer)

        if response["status"]:
          main_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "index":
        answer = input("Введите свой индекс: ")
        response = check_index(answer)

        if response["status"]:
          main_info[key] = int(deleteLetters(answer))
          break
        else:
          print(response["message"])

      if key == "address":
        answer = input("Введите свой адрес: ")
        main_info[key] = answer
        break

      if key == "add_info":
        answer = input("Введите дополнительную информацию, если нужно: ")
        main_info[key] = answer
        break
  update_data_main(main_info ,version)

def save_user_social_info (social_info):
  for key in social_info:
    while True:
      if key == "vk":
        answer = input("Введите свой id в Vk: ")
        response = check_social(answer)

        if response["status"]:
          social_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "telegram":
        answer = input("Введите свой id в Telegram: ")
        response = check_social(answer)

        if response["status"]:
          social_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "tiktok":
        answer = input("Введите свой id в TikTok: ")
        response = check_social(answer)

        if response["status"]:
          social_info[key] = answer
          break
        else:
          print(response["message"])
      if key == "youtube":
        answer = input("Введите свой id в YouTube: ")
        response = check_social(answer)

        if response["status"]:
          social_info[key] = answer
          break
        else:
          print(response["message"])
  update_data_social(social_info)

def save_user_empoloyer_info (employer_info):
  for key in employer_info:
    while True:
      if key == "ogrnip":
        answer = input("Введите ОГРНИП: ")
        response = check_ogrnip(answer)

        if response["status"]:
          employer_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "tin":
        answer = input("Введите ИНН: ")
        response = check_tin(answer)

        if response["status"]:
          employer_info[key] = int(answer)
          break
        else:
          print(response["message"])

      if key == "checking_account":
        answer = input("Введите расчетный счет: ")
        response = check_account(answer, "checking")

        if response["status"]:
          employer_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "bank":
        answer = input("Введите название банка: ")
        response = check_all_employer_point(answer)

        if response["status"]:
          employer_info[key] = answer
          break
        else:
          print(response["message"])

      if key == "bic":
        answer = input("Введите БИК: ")
        response = check_bic(answer)

        if response["status"]:
          employer_info[key] = int(answer)
          break
        else:
          print(response["message"])

      if key == "correspondent_account":
        answer = input("Введите корреспондентский счет: ")
        response = check_account(answer, "correspondent")

        if response["status"]:
          employer_info[key] = int(answer)
          break
        else:
          print(response["message"])
  update_data_employer(employer_info)

