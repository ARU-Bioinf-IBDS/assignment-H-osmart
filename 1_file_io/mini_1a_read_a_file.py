# instructions: write python to read the file example_in.txt
# and print out its contents to the screen.
# Hint: you will find what you need on the reference card
with open('example_in.txt') as in_file:
    contents = in_file.read()
print(contents, end='')
