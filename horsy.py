import time
import os

text = '''
_________________________________|\    /|____
_________________________________| \,,/_/____
___________________________---__/ \/    \____
____________________________--/     (D)  \___
___________________________ -/    (_      \__
_________________________// /       \_ /  -\_
_____-------_____--___--/           / \_ O o)
__/                                 /   \__/_
_/                                 /_________
||          )                   \_/\_________
||         /              _      /  |________
| |      /--______      ___\    /\  :________
| /   __-  - _/   ------    |  |   \ \_______
_|   -  -   /                | |     \ )_____
_|  |   -  |                 | )     | |_____
__| |    | |                 | |    | |______
__| |    < |                 | |   |_/_______
__< |    /__\                <  \____________
__/__\                       /___\___________

######################################################################################
#                                                                                    # 
#                            ,.--------._                                            #
#                           /            ''.                                         #
#                         ,'                \     |"\                /\          /\  #
#                /"|     /                   \    |__"              ( \\        // ) #
#               "_"|    /           z#####z   \  //                  \ \\      // /  #
#                 \\  #####        ##------".  \//                    \_\\||||//_/   #
#                  \\/-----\     /          ".  \                      \/ _  _ \     #
#                   \|      \   |   ,,--..       \                    \/|(O)(O)|     #
#                   | ,.--._ \  (  | ##   \)      \                  \/ |      |     #
#                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /     #
#                     '--'."      \                \              //     |____|      #
#                  /'    /         ) --.            \            ||     /      \     #
#               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /     #
#            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/      #
#          :###.-  |  ,/   /     \        /' ""\      .\        (     /              #
#         /####|   |   (.___________,---',/    |       |\=._____|  |_/               #
#        /#####|   |     \__|__|__|__|_,/             |####\    |  ||                #
#       /######\   \      \__________/                /#####|   \  ||                #
#      /|#######`. `\                                /#######\   | ||                #
#     /++\#########\  \                      _,'    _/#########\ | ||                #
#    /++++|#########|  \      .---..       ,/      ,'##########.\|_||  Donkey By     #
#   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\ Hard'96       #
#  /++++++|##########\.   '._        _,/       ,'######,''++++++++\                  #
# |+++++++|###########|       -----."        _'#######' +++++++++++\                 #
# |+++++++|############\.     \\     //      /#######/++++ S@yaN +++\                #
#      ________________________\\___//______________________________________         #
#     / ____________________________________________________________________)        #
#    / /              _                                             _                #
#    | |             | |                                           | |               #
#     \ \            | | _           ____           ____           | |  _            #
#      \ \           | || \         / ___)         / _  )          | | / )           #
#  _____) )          | | | |        | |           (  __ /          | |< (            #
# (______/           |_| |_|        |_|            \_____)         |_| \_)           #
#                                                                           19.08.02 #
######################################################################################

'''

iteration = 0
text_list = []
while True:
    text_list.append(text[iteration: iteration + 1])
    print("".join(text_list))
    iteration += 1
    time.sleep(0.001)
    os.system('cls' if os.name == 'nt' else 'clear')

    if iteration >= len(text): 
        break
print ("".join(text_list))

