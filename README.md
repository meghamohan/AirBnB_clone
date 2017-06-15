# HBNB - Holberton School - (Air BnB Clone)

![Hbnb](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Project Description:

+ This project is the initial foray into the world of Web Design / Development,as part of the Holberton School - Higher-level programming track, focusing solely on the back-end of our website

+ As such, it consists of building and implenting a command line interpreter and file storage back-end
to allow us, as developers, to manipulate and store data sans visual interface(GUI), similar to a shell

+ In effect, we are implementing a test environment to ensure our file storage system works, to later be migrated to a MySQL database


## Project Goals / Concepts Learned

+ Create a Python package
+ Create a command interpreter in Python using the `cmd` module
+ Learn Unit testing and how to implement it in a large project
+ How to write and read to/from a `JSON` file - serialization and deserialization (of a Class)
+ How to manage `datetime` and `UUID`
+ Utilizing `*args` and more specifically, `**kwargs` - to handle named arguments passed as function parameters


## Functionality

+ Creates an object (instance of defined BaseModel Class - as described below)
+ Implements data model of previously created instance
+ Store files in `JSON` format - via serialization and deserialization
+ Allows manipulation and management of objects/instances (via the following commands): 
  `create`, `update`, `destroy`,`new`, `all`
+ Other commands include:
  `show`, `help`, `quit`, `EOF`

## Usage / Execution


- To utilize our command line interpreter, please follow these steps (in order):

 + You must first clone the repository into your directory:
 +```
 +$ `git clone` https://github.com/halinav00/AirBnB_clone.git
 +```
 + To run the console, type `./console.py` script.
 +```
 + $ ./console.py
 +```
   Type `help` for list of commands.
 +```
 + (hbnb) help
 +
 + Documented commands (type help <topic>):
 + ========================================
 + EOF  all  create  destroy  help  quit  show  update
 +
 + (hbnb)
 + ```

## Create a Command Interpreter to manage your AirBnB objects that does following:
- Supports basic help, quit, exit and enter commands.
```
help
ctrl+d
quit
exit
enter
```
- Create a new object (ex: a new User or a new Place).
```
create <classname>
```
- Retrieve an object from a file, a database etc.
```
show <classname>
all
<classname>.count
<classname>.show
```
- Do operations on objects (count, compute stats, etc.).
```
<classname>.count
```
- Update attributes of an object.
```
update <classname> <id> <attribute_to_update> <updating_value>
```
- Destroy an object.
```
destroy <classname> <id>
```

### Environment
+ Our HBNB Clone has been interpreted/compiled/tested on `Ubuntu 14.04 LTS`
+ Written and tested utilizing `Python3 (Version 3.4.3)` and `PEP 8 Styling`


### Authors

*Megha Mohan* - [Github](https://github.com/meghamohan)

*Chris Novelli* - [Github](https://github.com/cnov20)

Feedback and/or contributions are welcome, please contact one or both of the project authors
