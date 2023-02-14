# method one to read a file
# file = open("text.txt")
# content = file.read()
# print(content)
# file.close()


# write to or create  a file
with open("text.txt", mode="a") as file:
    content = file.write("\nI love coding!!!!")
print(content)
