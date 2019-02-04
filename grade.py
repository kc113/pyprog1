import tkinter.filedialog
file_path = tkinter.filedialog.askopenfilename()
file = open(file_path,'r')
for line in file:
    print(line)


# read the gardes into a list

#count the grades per range

# write the histogram to the file
