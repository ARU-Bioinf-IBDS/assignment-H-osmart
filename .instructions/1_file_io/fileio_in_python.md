## Reading and writing files in Python Reference Card

* There are no extra modules necessary to read or write to
  a file in Python (so no need for any `import`).
* To access a disk file in Python you first need to open it
  with the `open()` function:
  ```python
  file_object = open(filename, mode)
  ```
  here 
  * `file_object` is the object returned by `open()` that
    allows the file to be accessed.
  * `filename` is a string giving the name of the file (for 
    example `sequence_abc.txt` or `/homes/fred/.config_abc`)
  * `mode` is a string indicating what you want to do with 
    the file.
