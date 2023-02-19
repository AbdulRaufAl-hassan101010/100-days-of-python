# method one to read a file
# file = open("text.txt")
# content = file.read()
# print(content)
# file.close()


# # write to or create  a file
# with open("text.txt", mode="a") as file:
#     content = file.write("\nI love coding!!!!")
# print(content)
"""
Automate a birthday invite letter that replaces the "[name]" in the  sample letter with the name provided in the names file and create new invite letter  for each name and save it in "the outputs/ready_to_send_invite" directory
"""
with open("./input/names/names.txt") as names_file:
    names_array = names_file.readlines()
    for name in names_array:
        # replace [name] in letter with name in names array
        with open("./input/letters/invite_letter.txt", mode="r") as letter_file:
            new_name = name.strip()
            new_letter = letter_file.read().replace("[name]", new_name)

            # save letters in "./output/ready_to_send_invite/letter_for_{new_name}.txt"
            with open(f"./output/ready_to_send_invite/letter_for_{new_name}.txt", mode="w") as automated_file:
                automated_file.write(f"{new_letter}")
