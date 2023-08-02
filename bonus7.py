filenames = ["1.doc", "1.gap", "1.present"]

filenames = [filenames.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)

