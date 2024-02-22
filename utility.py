import sys, time

def get_usr_in(task):
  cmd = input(f"*#/\\.-<>[{task}] ").lower()
  return cmd

def aes_render(str, delay=0.005):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()
