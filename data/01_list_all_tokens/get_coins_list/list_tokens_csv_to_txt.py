import pandas as pd
from data_processing.helpers import read_list_from_txt, write_list_to_txt
import os

df = pd.read_csv('list_tokens.csv')

l_all_tokens = df["url_name"].values.tolist()
print(l_all_tokens[:10])


print("The current working directory is:", os.getcwd())
os.chdir('..') # change the current working directory to the parent directory
# os.chdir('..')
# os.chdir('..')
print("The current working directory is:", os.getcwd())

# all_tokens = read_list_from_txt("all_tokens.txt")
# print(all_tokens)

# write_list_to_txt(l_all_tokens, "all_tokens.txt")

# with open("all_tokens.txt", "w") as f:  # Write the list of URLs to a file
#     f.writelines("%s\n" % token for token in l_all_tokens)
"""
,İstanbul Başakşehir Fan Token,i̇stanbul-başakşehir-fan-token
,Darüşşafaka Spor Kulübü Token,darüşşafaka-spor-kulübü-token
"""

encode_error_tokens = []
with open("all_tokens.txt", "w") as f:  # Write the list of URLs to a file
    for token in l_all_tokens:
        try:
            f.writelines(f"{token}\n")
        except UnicodeEncodeError:  # UnicodeEncodeError: 'charmap' codec can't encode character '\u0307' in position 1: character maps to <undefined>
            # import unicodedata
            # encoded_token = unicodedata.normalize('NFKD', token).encode('ascii', 'ignore').decode()
            # f.writelines(f"{encoded_token}\n")
            encode_error_tokens.append(token)

print(encode_error_tokens)
"""
['i̇stanbul-başakşehir-fan-token', 'ℓusd', 'darüşşafaka-spor-kulübü-token', 'gençlerbirliği-fan-token', 'balıkesirspor-token', 'babi̇l-token', 'i̇stanbul-wild-cats-fan-token', 'myōbu']
"""