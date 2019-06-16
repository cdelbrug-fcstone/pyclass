from tabulate import tabulate
import textfsm

template_file = "ex6_show_ip_bgp_summary.template"
template = open(template_file)

with open("ex6_show_ip_bgp_summary.txt") as f:
    raw_text = f.read()

parsed_template = textfsm.TextFSM(template)
parsed_output = parsed_template.ParseText(raw_text)
del parsed_output[-1]
template.close()

print(tabulate(parsed_output, headers=parsed_template.header, tablefmt="grid"))
