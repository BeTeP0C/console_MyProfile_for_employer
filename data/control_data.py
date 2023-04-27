import json

def get_data ():
  file = open("data.json", "r")
  data = json.loads(file.read())
  return data

def get_data_main (version):
  file = open("data.json", "r")
  data = json.load(file)
  main_info = data["default_main_info" if version == "default" else version == "business" and "business_main_info"]
  return main_info

def get_data_social ():
  file = open("data.json", "r")
  data = json.load(file)
  main_info = data["social_media"]
  return main_info

def get_data_employer ():
  file = open("data.json", "r")
  data = json.load(file)
  main_info = data["employer_info"]
  return main_info

def update_data_main (main_info, version):
  data = get_data()
  file = open("data.json", "w")
  data["default_main_info" if version == "default" else version == "business" and "business_main_info"] = main_info
  json.dump(data, file, indent=2)

def update_data_social (social_info):
  data = get_data()
  file = open("data.json", "w")
  data["social_media"] = social_info
  json.dump(data, file, indent=2)

def update_data_employer (employer_info):
  data = get_data()
  file = open("data.json", "w")
  data["employer_info"] = employer_info
  json.dump(data, file, indent=2)
