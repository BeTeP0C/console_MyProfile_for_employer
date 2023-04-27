def check_name (name):
  if len(name) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  elif len(name) < 2:
    return {
      "status": False,
      "message": "Минимум 2 символ!"
    }
  elif len(name) > 40:
    return {
      "status": False,
      "message": "Максимум 40 символов!"
    }
  elif any(symbol.isdigit() for symbol in name):
    return {
      "status": False,
      "message": "Имя не может содержать цифр!"
    }

  return {
      "status": True,
      "message": ""
    }

def check_age (age):
  if len(age) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  elif not(age.isdigit()):
    return {
      "status": False,
      "message": "Возраст должен быть числом. Попробуйте ещё раз!"
    }
  elif int(age) > 122:
    return {
      "status": False,
      "message": "Не врите, люди столько не живут!"
    }
  return {
      "status": True,
      "message": ""
    }

def check_phone (phone):
  if len(phone) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  elif phone[0] != "+":
    return {
      "status": False,
      "message": "Номер должен начинаться с '+!"
    }
  elif len(phone) < 12:
    return {
      "status": False,
      "message": "Вы не полностью ввел!"
    }
  elif len(phone) > 12:
    return {
      "status": False,
      "message": "Номер слишком длинны!"
    }
  elif not(phone.split("+")[1].isdigit()):
    return {
      "status": False,
      "message": "Номер должен состоять из циф!"
    }

  return {
      "status": True,
      "message": ""
    }

def check_mail (mail):
  if len(mail) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполения. Попробуйте еще ра!"
    }
  elif len(mail) < 3:
    return {
      "status": False,
      "message": "Минимум 3 символ!"
    }
  elif len(mail) > 320:
    return {
      "status": False,
      "message": "Максимум 320 символо!"
    }
  elif mail.find("@") == -1:
    return {
      "status": False,
      "message": "Некорректный ввод почт!"
    }
  return {
      "status": True,
      "message": ""
    }

def deleteLetters (str):
  new_str = ""
  for symbol in str:
    if symbol.isdigit():
      new_str += symbol

  return new_str

def check_index (index):
  if len(index) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  return {
    "status": True,
    "message": "",
  }

def check_social (id):
  if len(id) == 0:
    return {
      "status": True,
      "message": "",
    }
  elif len(id) < 3:
    return {
      "status": False,
      "message": "Минимум 3 символ!"
    }
  elif len(id) > 120:
    return {
      "status": False,
      "message": "Максимум 120 символ!"
    }
  elif id.find("@") == -1:
    return {
      "status": False,
      "message": "ID должен начинаться с '@'"
    }
  return {
    "status": True,
    "message": "",
  }

def PSAge (age):
  if age is None or age == "-" or len(age) == 0:
    return ""
  age = str(age)
  add_condition = not(age[-1:-3:-1][::-1] in ["11", "12", "13","14"])

  if age[-1] == "1" and add_condition:
    return "год"
  elif age[-1] in ["2","3","4"] and add_condition:
    return "года"

  return "лет"

def check_ogrnip (ogrnip):
  if len(ogrnip) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  elif not(ogrnip.isdigit()):
    return {
      "status": False,
      "message": "ОГРНИП должен состоять из цифр"
    }
  elif len(ogrnip) < 15:
    return {
      "status": False,
      "message": "ОГРНИП содержит 15 цифр"
    }
  return {
    "status": True,
    "message": "",
  }

def check_tin (tin) :
  if len(tin) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }

  elif not(tin.isdigit()):
    return {
      "status": False,
      "message": "ИНН должно стоять из цифр"
    }

  return {
    "status": True,
    "message": "",
  }

def check_bic (tin) :
  if len(tin) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }

  elif not(tin.isdigit()):
    return {
      "status": False,
      "message": "БИК должно стоять из цифр"
    }

  return {
    "status": True,
    "message": "",
  }

def check_account(account, view):
  if len(account) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  elif not(account.isdigit()):
    return {
      "status": False,
      "message": f'{"Расчетный" if view == "checking" else view == "correspondent" and "Корреспондентский"} счет должен состоять из цифр'
    }
  elif len(account) < 15:
    return {
      "status": False,
      "message": f'{"Расчетный" if view == "checking" else view == "correspondent" and "Корреспондентский"} счет содержит 20 цифр'
    }
  return {
    "status": True,
    "message": "",
  }

def check_all_employer_point (point):
  if len(point) == 0:
    return {
      "status": False,
      "message": "Это поле обязательно для заполнения. Попробуйте ещё раз!"
    }
  return {
    "status": True,
    "message": "",
  }

def check_for_emptiness(value):
  if value is None or len(str(value)) == 0:
    return "-"
  return value
