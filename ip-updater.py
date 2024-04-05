# Prompt the user to enter the new IP address
ip = input("Enter new IP: ")
print(ip)

# Construct the new 'connectip' line with the user-provided IP address
connect = 'connectip = {0} \n'.format(ip)

# Open the 'settings.ini' file in read mode
a_file = open("settings.ini", "r")
# Read all the lines in the file
list_of_lines = a_file.readlines()
# Replace the 73rd line (assuming the 'connectip' setting is at line 73) with the new 'connectip' line
list_of_lines[73] = connect

# Open the 'settings.ini' file in write mode
a_file = open("settings.ini", "w")
# Write the updated list of lines back to the file
a_file.writelines(list_of_lines)

# Prompt the user to press Enter to exit
exit = input("press enter to exit.")
print(exit)