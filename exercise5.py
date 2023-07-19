member = input("Write a name: ")
file = open("members.txt", "r")
existing = file.readlines()
file.close()
existing.append(member + "\n")
file = open("members.txt", "w")
existing = file.writelines(existing)
file.close()

