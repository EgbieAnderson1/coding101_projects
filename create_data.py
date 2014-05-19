#########################################################
# To be used with <wedding_rsvp.py> program
# Sunday 18 May 16:26:16 hrs
# Creates the data within the files on the user hard drive
#
# To be used in conjunction with RSVP class does not working
# on its own
#
########################################################

from wedding_rsvp import Interface
import os

rsvp = Interface()
#rsvp._load(os.path.join(os.getcwd(), "rsvp.txt"))                # load file
 
invitation_list = rsvp._get_invitation_list()                              #  guests on the invitation lists
confirmed_guests_list = rsvp._get_guests_attending()        # guests who are attending to the wedding
guests_not_attending = rsvp._get_guests_not_attending()  # guests not attending
guests_not_yet_replied = rsvp._get_guests_not_replied()   # guests not yet replied


file_path = os.path.join(os.getcwd(),"invitation_list.txt")    # create an invitation list file

# write the neccessary information to file
rsvp._write_to_file(file_path, "\n", mode="w")
rsvp._write_to_file(file_path, "#"*91)
rsvp._write_to_file(file_path, "\n[*]\t Shannon Morse WEDDING INVITATION LIST\n", "a")
rsvp._write_to_file(file_path, "\n[*] Invitation for the wedding of the year\n", "a")
rsvp._write_to_file(file_path, "\n[*] List of guests who have received an invitation to Shannon Wedding 2014.\n", "a")
rsvp._write_to_file(file_path, "\n\t[*] Note they might be multiple occurrence of the same name in the invitation list \n", "a")
rsvp._write_to_file(file_path, "\t[*] this is because some guests might share the same name\n\n", "a")
rsvp._write_to_file(file_path,"#"*91, "a")
rsvp._write_to_file(file_path,"\n\n", "a")
rsvp._write_to_file(file_path,"="*29 , "a")
rsvp._write_to_file(file_path,"\nGuests on the invitation list \n" , "a")
rsvp._write_to_file(file_path,"="*29 , "a")
rsvp._write_to_file(file_path, "\n\n[*] Names sorted in alphabetical order [*]\n", "a")
rsvp._write_to_file(file_path,"\n\n", "a")

# write information to invitation file
rsvp.write_in_block(file_path, invitation_list)  

# file path to the text file confirmed_guests_attending.txt
file_path = os.path.join(os.getcwd(), "confirmed_guests_attending.txt")

rsvp._write_to_file(file_path, "\n", mode="w")
rsvp._write_to_file(file_path, "#"*80)
rsvp._write_to_file(file_path, "\n[*]\t Shannon Morse WEDDING INVITATION LIST\n", "a")
rsvp._write_to_file(file_path, "\n[*] The guests who have confirmed their invitation\n", "a")
rsvp._write_to_file(file_path,"#"*80, "a")
rsvp._write_to_file(file_path, "\n\n\n", "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path,"Confirmed Guests" , "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path, "\n\n\n[*] Names sorted in alphabetical order [*]\n", "a")
rsvp._write_to_file(file_path,"\n", "a")
rsvp._write_to_file(file_path,"\n", "a")

# write guests who have confirmed their wedding invitation to file
rsvp.write_in_block(file_path, confirmed_guests_list)
    

# guests who are not coming to the wedding txt file path
file_path = os.path.join(os.getcwd(), "guests_not_attending_wedding.txt")

rsvp._write_to_file(file_path, "\n", mode="w")
rsvp._write_to_file(file_path, "#"*80)
rsvp._write_to_file(file_path, "\n[*]\t Shannon Morse WEDDING INVITATION LIST\n", "a")
rsvp._write_to_file(file_path, "\n[*] The guests who are not coming to the wedding\n", "a")
rsvp._write_to_file(file_path,"#"*80, "a")
rsvp._write_to_file(file_path, "\n\n", "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path,"Guests not attending wedding" , "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path, "\n\n\n[*] Names sorted in alphabetical order [*]\n", "a")
rsvp._write_to_file(file_path,"\n\n", "a")

# write guests who have confirmed their wedding invitation to txt file
rsvp.write_in_block(file_path, guests_not_attending)  

# file path to  guests who are not coming to a file
file_path = os.path.join(os.getcwd(), "guests_not_yet_replied.txt")

rsvp._write_to_file(file_path, "\n", mode="w")
rsvp._write_to_file(file_path, "#"*80)
rsvp._write_to_file(file_path, "\n[*]\t Shannon Morse WEDDING INVITATION LIST\n", "a")
rsvp._write_to_file(file_path, "\n[*] The guests who have not replied yet\n", "a")
rsvp._write_to_file(file_path,"#"*80, "a")
rsvp._write_to_file(file_path, "\n\n", "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path,"Guests who reply is pending" , "a")
rsvp._write_to_file(file_path,"="*12 , "a")
rsvp._write_to_file(file_path, "\n\n\n[*] Names sorted in alphabetical order [*]\n", "a")
rsvp._write_to_file(file_path,"\n\n", "a")

# write the guests who have not yet replied to file.
rsvp.write_in_block(file_path, guests_not_yet_replied)
