from data_processing.helpers import *
import constants as c


# class DataMaster:
#     def __init__(self):        # self.token_name = token_name        # self.all_tokens_to_crawl = all_tokens_to_crawl
#         xx = 1

def refresh_l_tokens():

    if c.RUN_DATE_HOUR == c.LAST_RUN_DATE_HOUR:
        pass
    else:  # c.RUN_DATE_HOUR != c.LAST_RUN_DATE_HOUR:
        last_l_tokens_path, last_l_done_tokens_path, last_l_error_tokens_path = c.get_l_tokens_paths(c.LAST_TOKEN_TO_CRAWL_PATH)
        append_txt_to_txt(last_l_done_tokens_path, c.ALL_DONE_TOKENS_PATH)
        append_txt_to_txt(last_l_error_tokens_path, c.ALL_ERROR_TOKENS_PATH)

        all_tokens = read_list_from_txt(c.ALL_TOKENS_PATH)
        all_done_tokens = read_list_from_txt_create_if_filenotfound(c.ALL_DONE_TOKENS_PATH)
        all_error_tokens = read_list_from_txt_create_if_filenotfound(c.ALL_ERROR_TOKENS_PATH)
        all_done_error_set = set(all_error_tokens + all_done_tokens)
        all_undone_tokens = [x for x in all_tokens if x not in all_done_error_set]
        write_list_to_txt(all_undone_tokens, c.ALL_UNDONE_TOKENS_PATH)

    #
    try:
        l_tokens = read_list_from_txt(c.L_TOKENS_PATH)
    except FileNotFoundError:
        # l_tokens = ['osmiumcoin', 'aptoslaunch-token', 'aptos', 'meta-apes-peel', 'moonstarter', 'bunnypark',                    'aptoslaunch-token', 'metaverse-vr']
        l_tokens = read_list_from_txt(c.ALL_UNDONE_TOKENS_PATH)[:100]  # TODO set this bigger?
        # TODO get from all_tokens - (all_error_tokens + all_done_tokens)
        write_list_to_txt(l_tokens, c.L_TOKENS_PATH)

    # try:
    #     l_done_tokens = read_list_from_txt(c.L_DONE_TOKENS_PATH)
    # except FileNotFoundError:
    #     open(c.L_DONE_TOKENS_PATH, 'w').close()
    #     l_done_tokens = []
    #
    # try:
    #     l_error_tokens = read_list_from_txt(c.L_ERROR_TOKENS_PATH)
    # except FileNotFoundError:
    #     open(c.L_ERROR_TOKENS_PATH, 'w').close()
    #     l_error_tokens = []

    l_done_tokens = read_list_from_txt_create_if_filenotfound(c.L_DONE_TOKENS_PATH)
    l_error_tokens = read_list_from_txt_create_if_filenotfound(c.L_ERROR_TOKENS_PATH)

    done_error_set = set(l_done_tokens + l_error_tokens)
    l_tokens = [x for x in l_tokens if x not in done_error_set]

    write_list_to_txt(l_tokens, c.L_TOKENS_PATH)

    # Write RUN_DATE_HOUR to the file
    with open(c.LAST_RUN_DATE_HOUR_PATH, "w") as f:
        f.write(f"{c.RUN_DATE_HOUR}")

    return l_tokens

def refresh_to_date(self):
    pass
