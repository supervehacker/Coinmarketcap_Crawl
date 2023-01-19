from data_processing.helpers import *
import constants as c


class DataMaster:
    def __init__(self):        # self.token_name = token_name        # self.all_tokens_to_crawl = all_tokens_to_crawl
        xx = 1

    def refresh_l_tokens(self):
        # l_tokens_path = f"{c.TOKEN_TO_CRAWL_PATH}/l_tokens.txt"
        # l_done_tokens_path = f"{c.TOKEN_TO_CRAWL_PATH}/l_done_tokens.txt"
        # l_error_tokens_path = f"{c.TOKEN_TO_CRAWL_PATH}/l_error_tokens.txt"

        try:
            l_tokens = read_list_from_txt(c.L_TOKENS_PATH)
        except FileNotFoundError:
            l_tokens = ['osmiumcoin', 'aptoslaunch-token', 'aptos', 'meta-apes-peel', 'moonstarter', 'bunnypark',
                        'aptoslaunch-token', 'metaverse-vr']
            # TODO get from all_tokens - (all_error_tokens + all_done_tokens)
            write_list_to_txt(l_tokens, c.L_TOKENS_PATH)

        try:
            l_done_tokens = read_list_from_txt(c.L_DONE_TOKENS_PATH)
        except FileNotFoundError:
            open(c.L_DONE_TOKENS_PATH, 'w').close()
            l_done_tokens = []

        try:
            l_error_tokens = read_list_from_txt(c.L_ERROR_TOKENS_PATH)
        except FileNotFoundError:
            open(c.L_ERROR_TOKENS_PATH, 'w').close()
            l_error_tokens = []

        done_error_set = set(l_done_tokens + l_error_tokens)
        l_tokens = [x for x in l_tokens if x not in done_error_set]

        write_list_to_txt(l_tokens, c.L_TOKENS_PATH)

        return l_tokens

    def refresh_to_date(self):
        pass
