from pathlib import Path

def generate_config():
  file = "./config.py"
  content = """
  # Generated with config_gen.py
  # Configure the needed stuff here

  
  # Bot's Discord token
  bot_token = ""
  # PostgreSQL database URL
  database_url = ""
  # Bot's text prefix
  prefix = ""
  # Array of extensions
  extensions = []
  """
  if not Path(file).exists():
    with open(file, "w") as f:
      f.write(content)
      print("[INFO] Configuration file generated successfully.")

  else:
    print("[WARNING] Configuration file already exists.")
