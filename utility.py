import sys, time

def get_usr_in(task="root"):
  cmds = input(f"*#/\\.-<>[{task}] ").lower()

  cmds = cmds.split(" ")
  # Note make a list of potential cmds, etc.
  for cmd in cmds:
    if cmd == 'query'
  debug(cmd)

def aes_render(str, delay=0.005):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def debug(item):
  print(f"debuging says: {item}")
