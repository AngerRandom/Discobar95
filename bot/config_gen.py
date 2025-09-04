from pathlib import Path

def generate_config():
  file = "./config.py"
  content = """
  # Generated with config_gen.py
  # Configure the needed stuff here

  bot_token = ""
  database_url = ""
  prefix = ""
  """
  if not Path(file).exists():
    with open(file, "w") as f:
      f.write(content)
      print("[INFO] Configuration file generated successfully.")

  else:
    print("[WARNING] Configuration file already exists.")
