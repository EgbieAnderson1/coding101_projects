########################################################################################
#
# Sunday 18 April 16:00hrs 2014
# Created by Egbie Anderson
#  Written using python 2.7
#  Copy right <None>
#
# Program Description
#  =================
#
# Does nothing by itself to be used with rsvp class in order to detect errors
#
#
#########################################################################################

from time import sleep
import sys

class Error(object):
    '''A class that displays the error that occurs running RSVP class'''
    
    def data_error(self):
        '''data_error(void) -> return(void)

        Displays data error that occurs with the rsvp.txt file
        '''
        
        print "\n[*] Incorrect formation in rsvp.txt file. Could not properly parse string"
        print "[*] Format must be in the form of '<name name-response>'"
        print "[*] Each grouping of names must then be followed with exactly one comma(,)"
        sys.exit("[*] Fix file format file and try again")

    def loading_error(self):
        '''loading_error(void) -> return(void)

        Displays data error that occurs when a file cannot be loaded
        '''
        print "\n[!] Failed to successfully load file."
        sleep(0.06)
        print "[!] Could not successful find the file rsvp.txt"
        sleep(0.06)
       
