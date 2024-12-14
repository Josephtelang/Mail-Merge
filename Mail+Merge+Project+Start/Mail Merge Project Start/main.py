PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names:
#     names = names.readlines()
#     print(names)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    
    
    for name in names:
        striped_name = name.strip()
        letter_filled = letter_contents.replace(PLACEHOLDER,striped_name)
        print(letter_filled)
        
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(letter_filled)