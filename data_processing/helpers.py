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
    with open(l_txt_path, "r") as f:  # Read a list from a file
        tokens = f.readlines()
    return [token.strip() for token in tokens]  # Strip newline characters and store the URLs in a list


def append_token_to_txt(token_name, l_txt_path):
    with open(l_txt_path, "a") as f:
        f.write(f"{token_name}\n")  # Write the text to a new line


def refresh_l_tokens():
    try:
        l_tokens = read_list_from_txt("l_tokens.txt")
    except FileNotFoundError:
        l_tokens = ['osmiumcoin', 'aptoslaunch-token', 'moonstarter', 'bunnypark', 'aptoslaunch-token', 'metaverse-vr']
        # with open("l_tokens.txt", "w") as f:  # Write the list of URLs to a file
        #     f.writelines("%s\n" % token for token in l_tokens)
        write_list_to_txt(l_tokens, "l_tokens.txt")

    try:
        l_done_tokens = read_list_from_txt("l_done_tokens.txt")
    except FileNotFoundError:
        open("l_done_tokens.txt", 'w').close()
        l_done_tokens = []

    try:
        with open("l_error_tokens.txt", "r") as f:
            l_error_tokens = read_list_from_txt("l_error_tokens.txt")
    except FileNotFoundError:
        open("l_error_tokens.txt", 'w').close()
        l_error_tokens = []

    done_error_set = set(l_done_tokens + l_error_tokens)
    l_tokens = [x for x in l_tokens if x not in done_error_set]

    write_list_to_txt(l_tokens, "l_tokens.txt")

    return l_tokens


def refresh_to_date():
    pass