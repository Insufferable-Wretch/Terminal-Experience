import utility as util
"""
aes_render(str, delay=0.005)
get_usr_in(task)
"""

import assets as ass

ass.print_banner(2)

# Terminal Loop
running = True
while running:
  cmd = util.get_usr_in()
  print(cmd)
  running = False
