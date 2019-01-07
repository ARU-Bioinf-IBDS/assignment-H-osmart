# Mini-exercise 1a. Read a text file and print out its contents.
##  Notes for making Run thru Video 
* Show them the reference card 
* Change to the appropriate directory
  ```
  cd IBDS
  cd assignment-H-osmart
  cd 1_file_io
  ```
* edit the first python
  ```
  edit mini_1a_read_a_file.py
  ```
  this task is to read a file and print out its contents.
* Lets first look at the input file:
  ```
  cat example_in.txt
  ```
* tell them to have a go on their own pausing the video.
* initial solution using open and close:
  ```python
  # instructions: write python to read the file example_in.txt
  # and print out its contents to the screen.
  # Hint: you will find what you need on the reference card
  in_file = open('example_in.txt')
  contents = in_file.read()
  in_file.close()
  print(contents)
  ```
  the `end=''` is necessary as contents has all the newlines in the file.
* run using:
  ```
  python mini_1a_read_a_file.py
  ```
* show that an extra new line is put in by print. Get rid of this by `end=''`
  ```python
  contents = in_file.read()
  in_file.close()
  print(contents,  end='')
  ```
* git commit the working solution with a suitable message - including copy/paste output showing
  python works.
* then say there is another cleaner way using `with` that automatically closes a file
  when you have finished:
  ```python
  with open('example_in.txt') as in_file:
      contents = in_file.read()
  print(contents,  end='')
  ```
* commit second version once again including output in the commit.
