import sys, time

def get_usr_in(task="root"):
  cmd = input(f"*#/\\.-<>[{task}] ").lower()
  cmd = cmd.split(" ")
  debug(cmd)

def aes_render(str, delay=0.005):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def debug(item):
  print(f"debuging says: {item}")
