
text = "Hi!\nYou successfully write a file!\nAmazing!"
text_2 = "You've appended some text.\nKeep it up!"

with open("test.txt", "a") as file:     # argument "w" is for writing, "r" for reading, "a" - append or add smth
    file.write(text_2)
