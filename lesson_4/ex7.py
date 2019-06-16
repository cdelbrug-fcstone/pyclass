import textfsm

template_file = "ex2_show_int_status.template"
template = open(template_file)

with open("show_int_status.txt") as f:
    raw_text = f.read()

re_table = textfsm.TextFSM(template)
parsed_output = re_table.ParseTextToDicts(raw_text)
template.close()

print(parsed_output)
