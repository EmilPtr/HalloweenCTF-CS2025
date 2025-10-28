import lock1
import lock2
import lock3
import lock4

print("Hello, my esteemed guest, I have trapped you within my sinister mansion, and you have...")
print("NO")
print("WAY")
print("OUT")
print("I will be back at dawn... and when I return, YOU SHALL BECOME THE DINNER!")
print("MUAHHAHAHAHAHAHAHAHAHAHAAHAHAHAHAH")

# Oh crap... I need to get out of here!
# Wait a second... What is this strange computer, and why does that door have 4 locks?

print("   /\\      /\\    |-------|  |---------")
print("  /  \\    /  \\   |       |  |        ")
print(" /    \\  /    \\  |       |  `````````|")
print("/      \\/      \\ |-------|  ---------|")
print("Welcome to MOS!")
print("Type the number of the lock you would like to get the code of:")

try:
    lock = int(input())
    if lock < 1 or lock > 4:
        print("Invalid lock... Exiting MOS")
        exit(1)
except ValueError:
    print("That's not a number... Exiting MOS")
    exit(1)

# Oh! I can try to get the locks' codes
# I can see how each password checker works too!
if lock == 1:
    lock1.attempt()
elif lock == 2:
    lock2.attempt()
elif lock == 3:
    lock3.attempt()
elif lock == 4:
    lock4.attempt()
