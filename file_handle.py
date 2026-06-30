f=open("batch.txt","w")
f.write("This is a sample text written to the file.\n")
f.close()
with open("batch.txt","w") as f:
    f.write("This is another sample text written to the file using 'with' statement.\n")
    f.write("This ensures that the file is properly closed after its suite finishes, even if an exception is raised.\n")
    f.write("You can write multiple lines to the file using the 'write' method.\n")
    f.write("Remember to always close the file after writing to it, or use the 'with' statement for better practice.\n")
    f.write("This is the last line of the sample text written to the file.\n")

    a="This is a sample text written to the file using a variable."

    f.write(a)

with open("batch.txt","r") as f:
    content = f.read()
    print(content)

with open("batch.txt","r") as f:
    for line in f:
        print(line.strip())

with open("batch.txt","a") as f:
    f.write("\nThis line is appended to the file using the 'append' mode.\n")
    f.write("Appending allows you to add content to the end of the file without overwriting existing content.\n")

with open("batch.txt","r") as f:
    f.read(10)
    print(f.tell())  # Get the current position of the file pointer

