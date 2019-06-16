from tabulate import tabulate
import textfsm

template_file = "ex4_junos_show_arp.template"
template = open(template_file)

with open("ex4_junos_show_arp.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

print(tabulate(data, headers=re_table.header, tablefmt="grid"))
