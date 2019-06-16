from pprint import pprint
import textfsm
from tabulate import tabulate

template_file = "ex4_junos_show_arp.template"
template = open(template_file)

# with open allows the automatic closing of the file and opening multiple files
with open("ex4_junos_show_arp.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
# Set the TextFSM template to a variable
re_table = textfsm.TextFSM(template)
# Parse the output file with the template
data = re_table.ParseText(raw_text_data)
# Close the open file
template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()

print("Printing a table")
print()

print(tabulate(data, headers=re_table.header, tablefmt="grid"))
