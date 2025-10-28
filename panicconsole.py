import hashlib

import passwordchecker


def panic_mode():
    print("****************************************WARNING-WARNING-WARNING****************************************")
    print("--------------------------------------MEMORY  CORRUPTION DETECTED--------------------------------------")
    print("--------------------------------------ENTERING KERNEL  PANIC MODE--------------------------------------")
    print("****************************************WARNING-WARNING-WARNING****************************************")
    print("Severe memory corruption has been detected and all systems have been shut down to prevent further catastrophic failure")
    print("A debugging shell with admin permissions has been started to help diagnose the issue.")

    while True:
        print("admin@MOS # ", end="")
        command = input()
        if command == "exit":
            print("Exiting MOS... Restarting computer...")
            exit(1)
        if command == "whatsmyname":
            print("MrEvilBurgurMan6767")
        if command == "recover":
            print("Recovering computer...")
            print("Recovering computer..")
            print("Recovering compuțer...")
            print("Recov3ring computer...")
            print("Recov3ring compu7er...")
            print("R3c0v3ring c0mputer..")
            print("R3c0v3r¡ng c0mpµt3r..")
            print("R3c0v3r!ng c0mpu±er..")
            print("R3c0v3r!nG c0mPµ†eR..")
            print("R3c0v3r!nG c0mPµ†eR..▒▒")
            print("R3c0v3r!nG c0mPµ†eR▒▒▓▓")
            print("R3c�v�ring c�mput�r ▒▓█")
            print("R��c���� computer ��▒▓██")
            print("���▒▓█ ███▒▓▓███ ☠☠☠")
            print("��█▓▒▐▌█▒▓▐▌░░▒▓█▌▐▐")
            exit(1)
        if command == "printlockcode4":
            lock_1 = input("Lock code 1: ").strip()
            lock_2 = input("Lock code 2: ").strip()
            lock_3 = input("Lock code 3: ").strip()
            if passwordchecker.check(1, lock_1) and passwordchecker.check(2, lock_2) and passwordchecker.check(3, lock_3):
                print("The code for lock 4 is: " +
                      hashlib.md5((lock_1+lock_2+lock_3).encode()).hexdigest())
            else:
                exit(1)
        if command == "unlockdoor":
            lock_4 = input("Lock code 4: ")
            if passwordchecker.check(4, lock_4):
                print("Unlocking door...")
                print("Unlocking door..")
                print("Unlocking doør...")
                print("Un1ocking door...")
                print("Un1ock1ng do0r...")
                print("Un10ck1n9 d00r..")
                print("Unl0cк1n9 d00r..")
                print("Unl0cк!n9 d0or..")
                print("Unl0cк!n9 d0or..▒")
                print("Unl0cк!n9 d0or..▒▓")
                print("Unl0cк!n9 d0or▒▓██")
                print("Uƞl0cк!n9 d0ʋr ▒▓█")
                print("U��l0c��!n9 d��r ▒▓██")
                print("���▒▓█ d��� ▒▓███ ☠")
                print("��█▓▒▐▌█▒▓▐▌░░▒▓█▌▐▐")
                print("WHAT")
                print("HOW CAN THIS BE???????????")
                print("YOU DEFEATED MY IMPENETRABLE SYSTEMS????????")
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
                print("DONT YOU RUN AWAY!!!!!!")
                print("COME BACK!!!!!!!!!!!!!!!!")
                print("----------------------------------------CONGRATULATIONS----------------------------------------")
                print("---------------------YOU HAVE ESCAPED! YOU HAVE COMPLETED THE ESCAPE ROOM!---------------------")
                print("------------------------------I hope you learned a thing or two ;]-----------------------------")
                print("-----------------------------------------------------------------------Made, with love, by Emil")