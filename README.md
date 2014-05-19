Program Description
  
  
 
 A simple program that takes a file called rspv.txt as input and displays the number of people
  attending, not attending and yet to reply
.
  In order for the program to work the following pre-condition must be met

     1)  The file name must be called rspv.txt
     2)  The file must not be empty at least a minimum of one name must be in the file.
     3)  The data in the file must be in the form of <name surname-response> separated by 
          a comma if there are more then one grouping of names.

     4) The response must either be 'yes' or 'no' or 'not replied'


  If none of these pre-condition are met the program will not start, but politely inform you 
  on how to solve the problem right before exiting.

  If all pre-condition are met the user can then view the following information:
    
        1) Number of people attending Shannon Wedding
        2) Number of people not attending Shannon weeding
        3) Those who have yet to replied all in alphabetical order.

      The program also includes a menu that allows the user of the program:
            1) To directly added names to the rsvp.txt text
            2) To look up names of guests who are attending, not attending or those who have not yet replied

  To use the program ensure that the following files are in the same directory
           1)  create_data.py
           2)  error.py
