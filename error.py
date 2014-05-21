########################################################################################
#
# Saturday 17 May 16:00hrs 2014
# Updated on wed 21 may 01:25 hrs
# Created by Egbie Anderson
# Updated on wed 21 May 01:57 hrs
#  Written using python 2.7
#  Copy right <None>
#
# Program Description
#  ==================
#
# Does nothing by itself to be used with rsvp class in order to detect errors
#
#
#########################################################################################

from time import sleep
from time import ctime
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
        print "[*] Fix file format file and try again"
        self.error_log("[!] {} : Failed to successful parse data from rsvp.txt file incorrect data format".format(ctime())) # create an error log
        raw_input("[*] Press any key to exit")
        sys.exit(0)
    

    def loading_error(self):
        '''loading_error(void) -> return(void)

        Displays data error that occurs when a file cannot be loaded
        '''
        print "\n[!] Failed to successfully load file."
        sleep(0.06)
        print "[!] Could not successful find the file rsvp.txt"
        self.error_log("[!] {} : Could not find rspv.txt file in user local directory.".format(ctime())) # create an error log
        print "[!] An error log has be created in your current working directory"
        sleep(0.06)

    def error_log(self, error):
        '''error_log(void) -> return(void)

        Create a log file detailing any errors that have occurred during
        the running of the program
        '''
        self.output = open("error_log.txt", "a")
        self.output.write(error)
        self.output.write("\n")
        self.output.close()
        
