'''#################################################################################
# 
# Coding 101 /Rsvp -> Example for episode 17
# Saturday 17 April 16:00hrs 2014
# Created by Egbie Anderson
# Written using python 2.7
# Copy right <None>
#
# Program Description
  ==============>
  
#  A simple program that takes a file called rspv.txt as input, if no file is found by that name 
#  the program creates that file and asks the user to use that file as a means to directly inteface
#  with the program.
#.
#  In order for the program to work the following pre-condition must be met
#
#   1)  The file name must be called rspv.txt
#   2)  The file must not be empty at least a minimum of one name must be in the file.
#   3)  The data in the file must be in the form of <name surname-response> separated by 
#         a comma if there are more then one grouping of names.
#
#   4) The response must either be 'yes' or 'no' or 'not replied'
#
#
#  If none of these pre-condition are met the program will not start, but instead inform you of
#  on how to solve the problem right before exiting.
#
#  If all pre-condition are met the information is then loaded into memory and the following
#   information can optionally be displayed to the user :
#    
#        1) Number of people attending Shannon Wedding
#        2) Number of people not attending Shannon weeding
#        3) Those who have yet to replied all in alphabetical order.
#
#      The program also includes a menu that allows the user of the program:
#            1) To directly added names to the rsvp.txt text
#            2) To look up names of guests who are attending, not attending or those who have not yet replied
#
#  To use the program ensure that the following files are in the same directory
#           1)  create_data.py
#           2)  error.py
#           3) You can use your own text file as long as it is called rsvp.txt, but providing
#                the data is entered in the way specified in the pre-condition above everything should run smoothly
#
#           4) Once every thing mention in step 1-3 are in the current working directory run the wedding_rsvp.py file
#
# The user of the program can modified alter or change the program
###################################################################################
'''

import os
import webbrowser
import create_data
from time import sleep
from error import Error
import sys

def sort_into_dictionary(wedding_list, guest_list):
    '''sort_into_dictionary(str, dictionary_object)

    Takes a grouping of strings and sorts them into
    a python dictionary object. A dictionary object is implemented
    using a hash function. This makes looking up objects extremely fast.
    Much faster then using a list object.
    '''
    error = Error()
    wedding_list = wedding_list.split(",")
    
    for guest in wedding_list:

        # ensure that the name before the dash is not empty
        try:
            name = guest.split("-")[0].strip().title()
            response = guest.split("-")[1].strip("\n").lower()
        except IndexError:
            error.data_error()
        else:

            # check that responses in rsvp file is not empty
            if not response or not name:
                error.data_error()

            # adds the names and replies to the dictionary object. If the name
            # already exists meaning that there is another guest with same name
            # append their reply to that name
            if name not in  guest_list.keys() :
               guest_list[name] = [response]
            else:
               guest_list[name].append(response)
   
        
###################################################
# Output class
###################################################
class InputOuput(Error):
    '''Responsible for creating , loading and writing to a file
    '''

    def __init__(self):
        self.guest_List = {}

    def create_file(self):
        '''creates an empty file with the name rsvp.txt'''

        print "\n[*] Creating a new file with called rsvp.txt"
        self.file = open("rsvp.txt", "w")
        self.file.close()
        
        print "[*] Successful created new file"
        
    def _load(self, rsvp_file):
        '''load(str) -> return(list)'''

        try:
             self.file = open(rsvp_file, "r")
        except IOError:
            
             self.loading_error()
             print "[*] Please wait attempting to create an empty file in user current working directory.."
             self.create_file()
             print "[*] Use that file to input you data, Thank you!!!\n"
             raw_input("[*] Press enter to exit program")
             sys.exit(0)
             
        else:
             self.wedding_list = self.file.read()
            
             # load names into a dictionary object this allows for a faster lookup
             sort_into_dictionary(self.wedding_list, self.guest_List)
             self.file.close()
            
    def _write_to_file(self, file_name, data=None, mode="a"):
        ''' _write_to_file(str, optional str, optinal str)

        Takes a string and appends to a file
        '''
        self.file = open(file_name, mode)
        self.file.write(str(data))
        self.file.close()
     
###################################################
# RSVP class
###################################################
class RSVP(InputOuput):
    ''' A simple program that takes a file called rspv.txt as input and displays the
       guests coming to a wedding, not coming or not yet replied. 
       The class contains only private methods.
    '''

    def __init__(self):
        InputOuput.__init__(self)
        self._load(os.path.join(os.getcwd(), "rsvp.txt"))

    def _set_guest_list(self, value):
        ''' _set_guest_list(value) -> return(void)
        Enables the dictionary object to be altered
        '''
        self.guest_List = value

    def flush(self):
        '''flush(void) -> return(void)

        Flushs out the contents of the dictionary object
        '''
        self._set_guest_list({})

    def _get_total_guests(self):
        ''' _get_total_guests(void) -> return(int)

        Returns the total number of people that have received an invitation.

        >>> _get_total_guests()
        15
        >>> _get_total_guests()
        5
        '''
        self.num1 = len(self._get_guests_attending())
        self.num2 = len(self._get_guests_not_attending())
        self.num3 = len(self. _get_guests_not_replied())

        return self.num1 + self.num2 + self.num3
    
    def _get_invitation_list(self):
        '''get_invitation_list(void) -> return(list)

        Returns a list of guests names that have receive an
        invitation to the wedding. Note they can be more then
        one guest who share the same name.

        '''
        # Take list and make into one big list
        self.invitation_list = self._get_guests_attending() + self._get_guests_not_attending() + \
                                        self. _get_guests_not_replied()
        
        self.invitation_list.sort()
        return self.invitation_list
        
    def _get_guests_attending(self):
        '''list_of_guest_attending(void) -> return(list)
        Returns the list of guests that have confirmed their invitation '''
        
        return self._lookup_guest_via_reply("yes")
        
    def _get_guests_not_attending(self):
        '''list_of_guest_not_attending(void) -> return(list)
        Returns the list of guests that are not attending'''

        return self._lookup_guest_via_reply("no")
        
    def _get_guests_not_replied(self):
        '''list_of_guest_not_replied(void) -> return(list)
        Returns the list of guests that have are not yet replied '''

        return self._lookup_guest_via_reply("not replied")
           
    def _lookup_guest_via_reply(self, confirmation):
        ''' _lookup_guest_via_reply(str)  -> return(list)

        Takes a str that is either 'yes', 'no' or 'not replied'
        and returns a list of guest based on that reply

        >>> _lookup_guest_via_reply('yes')
        ['Aunt Morses', 'Egbie Anderson', 'Keith Coffeman', 'Papa Coffeman', 'Shannon Morse']

         >>> _lookup_guest_via_reply('no')
        ['Aunt Morse']

        >>> _lookup_guest_via_reply('not replied')
        ['Egbie Anderson', 'Nana Morse', 'Shannon Morses']
        '''
        self.total_guests = self.guest_List.items() # get the dictionary items
        self.guests = []
       
        for guest in self.total_guests:
           self.names, self.replies = guest

           # iterate thru the replies if it matches the confirmation add to name to guests list
           for reply in self.replies:
               if reply == confirmation:
                   self.guests.append(self.names)
                                
        self.guests.sort()
        return self.guests
        
    def _get_replies(self, response, name):
        '''_get_replies(str, str) -> return(void)
        
        A helper function that adds additional help to
        _is_particular_guest_attending method by taking a name
        and a response and based on the response
        given prints out whether the person is attending the wedding.

        >>> _get_replies('no', 'Adam King')
        [*] Sorry Adam King will not be attending your weddding.

        >>> _get_replies('yes', 'Shannon Morse')
        [*] Shannon Morse will be attending your weddding.

        >>> _get_replies('not replied', 'Daddy Morse')
        [*] Daddy Morse has 'Not Yet Replied to your invitation.
        '''
        if response == "yes":
            print"[*] %s will be attending the weddding." %(name)
        elif response == "no":
            print"[*] Sorry %s will not be attending the weddding." %(name)
        else:
            print"[*] %s has 'Not Yet Replied to your invitation." %(name)
        
    def _is_particular_guest_attending(self, name, surname):
        '''_is_particular_guest_attending(str, str) -> return(void)

        Takes two strings a name and a surname and display whether
        the person is attending the wedding. If there are multiple occurrence
        of the same name meaning there are multiple guests that share same name,
        the program prints out each name and assign to them a unique ID number.
        
        Uses the helper function _get_replies.

        >>> _is_particular_guest_attending(Shannon, Morse)
        [*] Shannon Morse will be attending your weddding.

        >>> _is_particular_guest_attending(Daddy, Morse)
        [*] Daddy Morse has 'Not Yet Replied to your invitation.

        >>> _is_particular_guest_attending(Aunt, Morse)
        [*] Sorry Aunt Morse will not be attending your weddding.

        >>> _is_particular_guest_attending(Egbie, Anderson)
        [*] There are 3 guests by the name of Egbie Anderson on the invitation list.

        [*] Sorry Egbie Anderson    ID No #: 1 will not be attending the weddding.
        [*] Egbie Anderson    ID No #: 2 has 'Not Yet Replied to your invitation.
        [*] Egbie Anderson    ID No #: 3 will be attending the weddding.

        '''
        # look up guests retreive their replies 
        try:
            self.response = self.guest_List["%s %s"%(name.title(), surname.title())]
        except KeyError:
            print "[*] The name %s %s is not in your wedding invitation." %(name.title(), surname.title())
        else:
        
            self.name = name.title() + " " + surname.title()
            self.guests_with_same_name = len(self.response) # no of guest with same name

            self.response.sort() 

            # if there is one guest with that name get their reply.
            if self.guests_with_same_name == 1:
                self._get_replies(self.response[0], self.name)
                
            else:
                print "\n[*] There are %d guests by the name of %s on the invitation list.\n" %(self.guests_with_same_name, self.name)

                # since there are more then one guest that share the same name
                # iterate thru the list of responsible and display each guest along with their reply
                for i in range(len(self.response)):
                   self._get_replies(self.response[i], self.name + "    ID No #: " + str(i + 1))

            
############################################################################
# User interface class
############################################################################
class Interface(RSVP):
    '''The interface class acts as a bridge between the various
    classes and also allows the user of the program access to
    the menu interface function
    '''
    def __init__(self):
          RSVP.__init__(self)
         
    def _open_file(self, file_name):
         '''_open_file(str) -> return(void)

        Takes a file name and opens the file
         '''
         webbrowser.open(file_name)
         
    def write_in_block(self, file_path, file_list):
        '''write_in_block(str, list) -> return(void)

        Works similar to write_to_file method. The
        only difference is instead of writing single
        lines to a file. The method can write a block
        of strings to a file at once
        '''
      
        for names in file_list:
            self._write_to_file(file_path, "[*] "+names)
            self._write_to_file(file_path,"\n")
               
    def _inform_user(self, state):
        ''' _inform_user(str) -> return(void)
        Informs the user of the state of the program
        '''
        print "[*] Displaying %s in sorted alphabetically order." %(state)
        sleep(0.02)
        print "[*] Please wait opening file in new window..."
        
    def menu(self):
        '''menu(void) -> return(void)

        An interactive menu that can be used by the user
        '''
        while True:
            
            print """

            [*] SHANNON MORSE WEDDING MENU LIST 2014\n
            <====================================>
            
            \n\t\tMENU OPTIONS
                ==============

            \t[1] Wedding Invitation list
            \t[2] Guests attending wedding
            \t[3] Guests not attending wedding
            \t[4] Guests who have not yet replied
            \t[5] Look up particular guests
            \t[6] Add Guest
            \t[7] How many people coming to the wedding?
            \t[8] Exit

            <======================================>
            """
            
            try:
                self.choice = int(raw_input("\n[*] Selection your option : "))
            except ValueError:
                print"[*] Choice must be 1-8"
            else:
                return self.choice
            
    def _look_up_guest(self):
        ''' _look_up_guest(void) -> return(void)

        Looks up a guest on the invitation list and displays if there are attending
        the wedding.
        '''
        print "\n[*] Enter a name in order to lookup whether a guest is attending.\n"
        
        self.first_name = raw_input("[*] Enter the firstname : ")
        self.surname = raw_input("[*] Enter the surname : ")
        self._is_particular_guest_attending(self.first_name, self.surname)

    def _open_wedding_invitation_file(self):
        '''_open_wedding_invitation_file(void) -> return(void)
        Opens the invitation guests list file
        '''
        self._open_file(os.path.join(os.getcwd(), "invitation_list.txt"))

    def _open_attendees_file(self):
        '''_open_attendees_file(void) -> return(void)
        Opens the list of attendees attending the wedding file
        '''
        self._open_file(os.path.join(os.getcwd(), "confirmed_guests_attending.txt"))

    def _open_guests_not_coming_file(self):
        '''_open_guests_not_coming_file(void) -> return(void)
        Opens the guest not coming file.
        '''
        self._open_file(os.path.join(os.getcwd(), "guests_not_attending_wedding.txt"))

    def _open_not_replied_file(self):
        '''_open_not_replied_file(void) -> return(void)
        Opens the guest not replied file
        '''
        self._open_file(os.path.join(os.getcwd(), "guests_not_yet_replied.txt"))

    def format_string(self, first_name, surname, response):
        '''format_string(str, str, str) -> return(str)

        Takes three strings a name, surname and a response and concatenates
        them in the form of <,name surname-response>. The comma at the
        beginning ensures that when appended to the rspv.txt file the name infront
        of it is separated with a comma.

        >>> format_string(shannon, morse, yes)
        ',Shannon Morse-yes'
        '''
        return ("," + first_name.title().lstrip() + " " + surname.title() + "-" + response.strip())

    def update(self):
        """update(void) -> return(None)

        The update method updates the files in memory as well as the file on the hard drive.
        Since a dictionary object is mutable and the program does not exists when the new
        files are updated in memory. This means that the dict object contains the old records
        and if the new updated file is loaded into the dictionary object there will be duplicate records
        
        The flush method ensures that the dictionary object is flushed out before the new
        data is loaded into the dictionary method. This ensures that there are no duplicate
        records in the dictionary object
        """
        print "[*] Please wait updating files..."

        reload(create_data) # allows the files in the hard drive to updated in real time
        self.flush()
        self._load(os.path.join(os.getcwd(), "rsvp.txt"))
                     
        print "[*] Update successful\n"

    def _get_total_people_invited(self):
        ''' _get_total_people_attending(void) -> returns(None)

        Prints the total number of people on the invited list.

        >>> _get_total_people_invited()
        [*] The total number of people invited to the wedding is : 4
        '''
     #   self.update() # run update to get any new information
        self.num_of_people_invited =  self._get_total_guests()
            
        print '\n[*] The total number of people invited to the wedding is :  %d \n '%(self.num_of_people_invited)
        print '[*] Out of %d people invited number of people not attending are   : %d' %(self.num_of_people_invited, len(self._get_guests_not_attending()))
        print '[*] Out of %d people invited number of people attending are       : %d' %(self.num_of_people_invited, len(self._get_guests_attending()))
        print '[*] Out of %d people invited number of people not yet replied are : %d\n' %(self.num_of_people_invited, len(self._get_guests_not_replied()))
        
    def _add_guest(self):
        '''add_guest(void) -> return(void)

        Enables the user of the program to add a name to the invitation list

        >>> add_guest()
        
        [*] Enter a first name, surname, and whether they are attending wedding"
        [*] Enter the first name: jacob lisa maria
        [*] Enter the surname: victoria
        [*] Enter confirmation as either 'yes', 'no' or not 'not replied' : yes
        [*] Added Jacob Lisa Maria Victorua to the wedding list"
        
        '''
        print "\n[*] Enter a first name, surname, and whether they are attending wedding"

        self.possible_responses = ["yes", "no", "not replied"]
        
        # First while loop ensures that first name is never empty
        while True:
            
            self.first_name = raw_input("[*] Enter the first name:  ")
            self.surname = raw_input("[*] Enter the surname      : ")

            # Ensure that names are not empty
            if not self.first_name and not self.surname:
                continue
            
            # make sure that names are alphanumeric characters
            if self.first_name.isalpha() and self.surname.isalpha():
                break
            
        # second for loop ensures that confirmation is either yes, no or not replied
        while True:
            self.confirmation = raw_input("[*] Enter confirmation as either 'yes', 'no' or 'not replied' : ")
            self.name = self.first_name.title() + " " + self.surname.title()

            # check whether the response matchs specification if not ask for response again
            if self.confirmation.lower() not in self.possible_responses:
                continue
              
            self.formatted_string = self.format_string(self.first_name, self.surname, self.confirmation.lower())
            break

        self._write_to_file("rsvp.txt", data=self.formatted_string)
        print "[*] Added %s to the wedding list\n"%(self.name)

        self.update() # update files each time a new entry is added
       
# the main program
def main():

    # call the menu interface class
    while True:
             
        choice = user_interface.menu()
        
        if  choice == 1:
            user_interface._inform_user("guests who receive an invitation")
            user_interface._open_wedding_invitation_file()

        elif choice == 2:
             user_interface._inform_user("all guests attending wedding")
             user_interface._open_attendees_file()
           
        elif choice == 3:
             user_interface._inform_user("all guests not attending wedding")
             user_interface._open_guests_not_coming_file()

        elif choice == 4:
             user_interface._inform_user("all guests not yet replied")
             user_interface. _open_not_replied_file()

        elif choice == 5:
             print '[*] Looking up guests ...'
             user_interface._look_up_guest()

        elif choice == 6:
              user_interface._add_guest()

        elif choice == 7:
             user_interface._get_total_people_invited()

        elif choice == 8:
            sys.exit("Exiting program, Goodnight Sweet Prince !!!")

        else:
            print '[*] choice must be between 1-7'
            continue
        
        raw_input("\n[*] Press enter to continue")
        
# if the program is run and not imported the main class is called         
if  __name__ == "__main__":

   user_interface = Interface()
   main()
