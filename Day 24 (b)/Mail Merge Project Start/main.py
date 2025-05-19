#TODO: Create a letter using starting_letter.txt

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os

# Paths
names_path = "./Input/Names/invited_names.txt"
letter_template_path = "./Input/Letters/starting_letter.txt"
output_dir = "./Output/ReadyToSend"

# Step 1: Read all names
with open(names_path) as names_file:
    names = names_file.readlines()

# Step 2: Read the letter template
with open(letter_template_path) as letter_file:
    letter_template = letter_file.read()

# Step 3: Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Step 4: Create and save a personalized letter for each name
for name in names:
    stripped_name = name.strip()  # Remove any whitespace and newlines
    personalized_letter = letter_template.replace("[name]", stripped_name)

    output_path = f"{output_dir}/letter_for_{stripped_name}.txt"
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(personalized_letter)

print("✅ All letters have been created successfully in the 'ReadyToSend' folder!")
