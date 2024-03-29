import utility as util

def print_banner(selector=0):
  banners = [
    """
/  -----------------------------------------  \\
 |                                           |
 |   OsmiUm 1(0.11.5)  ///  Welcome, User
                                             |
 |                                           |
\\  -----------------------------------------  /
    """,


    """
[*] ............................................. *
                                        ----/----
    |
]|      OsmiUm 2(0.11.5)  ---  Welcome, User      |[
                                               |
   ----\\----
 * ............................................. [*]
    """,


    """
__                                               __
  \\        ________  __                            \\
  |                      \                         |
  |                       -\|                      |
  |      OsmiUm 3(0.11.5)  /-\  Welcome, User      |
   |\\ -                    \-/                  _ / |
   |/ -                     |\-                  \\\\ |
  |                            \  __  ________     |
    """
  ]

  util.aes_render(banners[selector])
