
## 1. What difference
The difference between this implementation of grep in python from others
1) Searches for different types of input data without specifying the type
- List[str]
- TextIOWrapper: Opened files
- str: Single-line and multi-line strings
- str: Just file paths like `dir/filename.txt`
2) Works primarily inside the python code and returns a List[str] type that is convenient for further processing
3) Has an unlimited number of input parameters
4) By default, it works with normal (extended) regular expressions
Yes - you can simple write in python code:
```python
pattern = r"hello"
str_variable = "hello world"
list_variable = ["hello there", "general kenobi"]
file_path = "test_file.txt" # File contain: "This is a test file.\nhello from file\nAnother line."
result = grepli(pattern, str_variable, list_variable, file_path)
print(result)
```
And you get sum result:
```python
['hello world', 'hello there', 'hello from file']
```
> See this test code with this example: https://github.com/linxuil/grepli/blob/main/tests/test_grepli.py#L45

## 2. General info
This project is grep function implementation for python.
I use this "grepli" function for:
- Analyse log files in tests where i need info from linux
  - tcpdump
  - dmesg
  - journalctl
  - <'etc...'>
- Gateway from files in file system to list type in python
  if run with dot regex `grepli . 'filepath.txt'`

## 3. Usage
### 3.1. Without install module
Try use python script via cmd without install:
```bash
$ cd <'prj_folder'>

[prj_folder]$ TST_MULTILINE_VAR='first tested line
second line test
third line'

[prj_folder]$ /bin/python3 console_scripts/main.py 'foo|text.$' foo_yes 'bar_no' 'text. not last' 'last text.' 'tests/pre_created_file.txt' "${TST_MULTILINE_VAR}"

['foo_yes', 'last text.', 'This is a test text.']
```
### 3.2. PIP module istall
You can install via `pip` in venv:
```bash
# Pull repo
$ REPO_URL='https://github.com/linxuil/grepli'&&\
git clone "${REPO_URL}" 'grepli'&&\
cd grepli

# Install venv if needed
$ sudo apt install python3-venv

# Create and activate venv in directory "venv"
$ VENV_DIR_NAME='venv'&&\
python3 -m venv "${VENV_DIR_NAME}"&&\
source venv/bin/activate

# Install module
$ pip install -e .

# Try use console command
$ grepli '\b\w{4}\b' 'text with 4 letters wods' 'text_test' 'tests/pre_created_file.txt'
```
This command show output contain:
- One string from input parameters
- Two lines from file `tests/pre_created_file.txt`
```
['text with 4 letters wods', 'This is a test text.', 'Text like short life 123.']
```
Then you need exit from venv
```
$ deactivate
```

<!-- CONTRIBUTING -->
## 4. Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YouFeature`)
3. Write any changes in code
4. Add changes to index (`git add -A`)
5. Commit your Changes (`git commit -m 'You description'`)
6. Push to the Branch (`git push origin feature/YouFeature`)
7. Open a Pull Request on github

## 5. License

Distributed under the MIT License. See `LICENSE.md` for more information.

## 6. Contact

linxuil - linxuil.g@gmail.com

Project Link: [https://github.com/linxuil/grepli](https://github.com/linxuil/grepli)
