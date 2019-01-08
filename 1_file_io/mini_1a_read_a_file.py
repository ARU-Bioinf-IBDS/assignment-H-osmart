# instructions: write python to read the file example_in.txt
# and print out its contents to the screen.
# Hint: you will find what you need on the reference card
in_file = open('example_in.txt')
contents = in_file.read()
in_file.close()
print(contents, end='')
