import hashlib
import array

import panicconsole

def attempt():
    print("Did you really think you would get so far? That you could...")
    print("ESCAPE???????")
    print("MUAHAHAHAHHAHAAHAHAHA")
    print("NEVER!!!!!!!!!!!!!")
    print("This feeble program just echoes stuff back to you!!!!!")
    print("You shall never get the 4th lock!!!!! NYEHEHEHEHEHEHEHEHEHEHEHEH")

    # Oh crap there's gotta be a way!!!

    while True:
        try:
            inp = input()

            if len(inp) > 256:
                maxi = 256
            else:
                maxi = len(inp)

            echo_back = ""

            for i in range(maxi):
                echo_back += inp[i]

            for c in range(0, len(inp)):
                print(echo_back[c], end="")
            print()

        except IndexError:
            print()
            print()
            print()
            panicconsole.panic_mode()
            pass
