pressed = input("")
displayed = input("")

silly = ""
silly_display = ""
quiet = ""
if len(pressed) == len(displayed):
    for i in range(len(pressed)):
        if pressed[i] != displayed[i]:
            silly = pressed[i]
            silly_display = displayed[i]
elif len(displayed) < len(pressed):
    for i in range(len(pressed)):
        if pressed[i] != displayed[i] and displayed[i] == pressed[i+1]:
            quiet = pressed[i]
            break

print(f"{silly} {silly_display}")
print(f"{quiet}")
