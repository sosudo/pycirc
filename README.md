# PyCirc
A Python library for the Circulates Bitwise Shift Operators (rcirc and lcirc)

# Directions
To use this library, just add the ```circ.py``` file to the directory you need the functions in, and then import it using ```import circ```.
<br>
You can call its functions by ```circ.rcirc(a,b)``` and ```circ.lcirc(a,b)```.
<br>
For an example, refer to ```example.py```.
<br>
The argument ```a``` in the function is an integer which represents how many times the bit-string is circulated, and the argument ```b``` is an integer which represents the bit-string you are circulating.<br>
Note that the argument ```b``` must be a string if its leading digit is 0.<br>
Therefore, the best practice is to treat argument ```a``` as an integer and argument ```b``` as a string.
