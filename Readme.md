### Instructions
   1. update python to 3.x.x
       - verify by running $ python --version in the terminal
   2. using applcore start logging from the GEA2/3 tab and save the log file.
   3. run python applcoreResponseData.py <filepath to applcore log> <ERD to filter(optional)>
   4. read results in terminal and a new csv will be in the "Results" directory.
   5. if no arguments are passed in, the program will run with a default hard coded .csv file (for testing).

Additional Notes:
    - program only reads the RX values (response only data)
    - on the ~apex~ program sometimes multiple TX values will show up sequentially, meaning no response from the MC
    - currently this program only supports a u16 response

TODO:
    - add functionality for other data types


Example: 
$ python applcoreResponseData.py "./applcoreLogs/CoolingFan_selfClean_2022-02-25T13-14-22.545_1.csv"



