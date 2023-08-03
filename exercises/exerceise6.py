filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for i in filenames:
    file = open(i, "w")
    file.write("Hello")
    file.close()
