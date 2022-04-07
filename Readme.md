### Instructions
This command line program is best used to record cooling fan speed or RTD temperature over time, it will handle any 2 byte data

#### Requirements
1. update python to 3.10.x+, update pip to match the python version
       - verify by running $ python --version in the terminal2.
2. run $ pip install -r requirements.txt

Create a folder "Results" inside where this program is located.
   1. using applcore start logging from the GEA2/3 tab and save the log file.
   2. run python applcoreResponseData.py <filepath to applcore log> <ERD to filter(optional)-not really working well>
   3. read results in terminal and a new csv will be in the "Results" directory.
   4. if no arguments are passed in, the program will run with a default hard coded .csv file (for testing).

Additional Notes:
    - Shows % of data lost, calculates the number of TX vs RX
    - currently this program only supports a u16 response

TODO:
    - add functionality for other data types


Example: 
$ python applcoreResponseData.py "RC17ReadRTD5MinExample.csv"



