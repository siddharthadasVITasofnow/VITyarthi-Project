###### Morse Code Converter:-



Name: Siddhartha Das  
Registration number: 26BEC10115  
Course: CSE1021 Introduction to Problem Solving and Programming  
University: VIT Bhopal



###### Overview:-



A Python program that converts text to Morse code, converts Morse code back to text, and shows the Morse signal as a pattern of ON/OFF time units. It is built with the concepts of CSE1021: functions and modules, conditionals, loops, lists, tuples, sets and dictionaries, and simple algorithms such as counting, summation and reversal (lookup).



###### Features:-



* Module 1, Encoder: text to Morse code (letters `a-z`, `A-Z`, digits `0-9`, spaces between words)
* Module 2, Decoder: Morse code to text (words separated by `/` or three spaces)
* Module 3, Signal pattern: shows the Morse signal using standard timing (dot = 1 unit, dash = 3, letter gap = 3, word gap = 7) and counts ON units and total units
* Input validation: empty input, unsupported characters and invalid Morse code give a clear error message instead of a crash
* Session log: records every action of the session and counts successes and errors

###### Technologies Used:-

* Python 3 (basic features only, no external libraries)
* Git and GitHub



###### Relation to the CSE1021 Syllabus:-



|Syllabus topic:|Where it is used:|
|-|-|
|Top-down design, algorithms, flowchart, pseudo-code (Unit 1)|Program is split into modules; workflow diagram in ,`docs/diagrams.md`|
|Modules and functions, parameters, tuple assignment, comments (Unit 2)|Every file is a module of functions; `valid, message = check\_text(text)`|
|Conditionals, iteration, `while`, `for`, `break`/`continue` (Unit 3)|Menu loop, `if/elif/else`, loops in encoder, decoder and signal|
|Counting and summation (Unit 3, Unit 5)|`count\_status()` and `total\_duration()`; ON-unit count in `show\_signal()`|
|Dictionaries (Unit 5)|`morse\_code` and `reverse\_morse\_code` in `morse\_map.py`|
|Lists, tuples, sets (Unit 5)|Lists of tokens and signal units; tuples returned by every check; a set collects unsupported characters|
|||

###### 

###### Project Structure:-


morse-converter/
├── README.md
├── statement.md
├── requirements.txt
├── src/
│   ├── morse\_map.py      # Morse dictionary and reverse dictionary
│   ├── encoder.py        # Module 1: text -> Morse
│   ├── decoder.py        # Module 2: Morse -> text
│   ├── morse\_signal.py   # Module 3: signal pattern (ON/OFF units)
│   ├── validator.py      # input checks and error messages
│   ├── logger.py         # session log
│   └── main.py           # menu-driven program
├── tests/
│   ├── test\_encoder.py
│   ├── test\_decoder.py
│   └── test\_validator.py # validator and signal tests
└── docs/
    └── diagrams.md       # architecture, workflow, use case, sequence, class/component diagrams


###### How to Install and Run:-



1. Install Python 3.
2. Download or clone this repository:


   git clone <your-repository-url>
   cd morse-converter
  

3. Nothing else needs to be installed.
4. Run the program from the project folder:


   python src/main.py
   

5. Choose an option from the menu (1 to 5).



###### Example:-


Choose an option (1-5): 1
Type your text: Hello 123
Morse code: .... . .-.. .-.. --- / .---- ..--- ...--

Choose an option (1-5): 3
Type your text: sos
Morse code: ... --- ...
Signal (# = ON, \_ = OFF):
#\_#\_#\_\_\_###\_###\_###\_\_\_#\_#\_#
ON units: 15 | Total units: 27


Invalid input shows an error and the menu continues:



Type your text: hi #
Error: Unsupported character(s): #


###### Testing:-



Run these from the project folder (each prints PASS for every test):


python tests/test\_encoder.py
python tests/test\_decoder.py
python tests/test\_validator.py


