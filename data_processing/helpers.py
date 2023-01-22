import json


def write_to_json(dic: dict, json_path: str):
    with open(json_path, 'w') as f:
        json.dump(dic, f)


def read_from_json(json_path):
    with open(json_path, "r") as f:
        dic = json.load(f)
    return dic


def write_list_to_txt(l_tokens, l_txt_path) :
    with open(l_txt_path, "w") as f:  # Write the list of URLs to a file
        f.writelines("%s\n" % token for token in l_tokens)


def read_list_from_txt(l_txt_path):
    with open(l_txt_path, "r", encoding="ISO-8859-1") as f:  # Read a list from a file
        tokens = f.readlines()
    return [token.strip() for token in tokens]  # Strip newline characters and store the URLs in a list


def read_list_from_txt_create_if_filenotfound(l_txt_path):
    try:
        l_tokens_x = read_list_from_txt(l_txt_path)
    except FileNotFoundError:
        open(l_txt_path, 'w').close()
        l_tokens_x = []
    return l_tokens_x


def append_element_to_txt(element_to_append, l_txt_path):       #element_to_append ~ token_name, url
    with open(l_txt_path, "a") as f:
        f.write(f"{element_to_append}\n")  # Write the text to a new line


def append_txt_to_txt(infile_path, outfile_path):
    with open(outfile_path, "a") as outfile:
        with open(infile_path) as infile:
            for line in infile:
                outfile.write(f"{line}")


