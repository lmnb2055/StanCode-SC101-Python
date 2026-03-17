"""
File: anagram.py
Name: Sidney
The warmest and kindest TA: Jenny
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    see the number of anagrams for each word and calculate the time of running
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        dict_set = read_dictionary()
        if s == EXIT:
            break
        start = time.time()
        find_anagrams(s, dict_set)
        end = time.time()
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():   # dict的bigO比較快
    set_dictionary = set()
    filepath = 'dictionary.txt'
    with open(filepath, 'r')as f:
        for line in f:
            set_dictionary.add(line.strip())
        return set_dictionary
        #dict_lst.append(line.replace('\n', ''))  # strip  ///// 有逗點空白才會用replace
        # return dict_lst


def find_anagrams(s, dict_set):
    """
    :param s: the word which the user type
    :return: X
    """
    print("Researching...")
    lst_s = []
    for i in range(len(s)):
        # lst_s['s', 't', 'o', 'p']
        lst_s.append(s[i])
    ana_lst = []  # 有一個記憶體位址
    find_anagrams_helper(s, [], lst_s, ana_lst, dict_set, [])
    print(str(len(ana_lst)) + " anagrams: ", end="")
    print(ana_lst)


    # print("Researching...")
    # ana_lst = []
    # find_anagrams_helper(s, '', ana_lst)
    # print(str(len(ana_lst)) + " anagrams: ", end="")
    # print(ana_lst)


def find_anagrams_helper(s, current_lst, lst_s, ana_lst, dict_set, index_lst):

    if len(current_lst) == len(s):
        ana = "".join(current_lst)
        if ana in dict_set and ana not in ana_lst:
            print('Found: ' + ana)
            ana_lst.append(ana)
            print("Researching...")
    else:
        for i in range(len(lst_s)):
            if i not in index_lst:
                current_lst += lst_s[i]
                index_lst.append(i)    # 把i存入Index_lst裡面（eg. 2, 6）
                find_anagrams_helper(s, current_lst, lst_s, ana_lst, dict_set, index_lst)
                current_lst.pop()
                index_lst.pop()
            '''
            較花時間
            alphanum_in_current_str = current_lst.count(alphabet)
            alphanum_in_str = lst_s.count(alphabet)
            if alphanum_in_current_str < alphanum_in_str: # 重複字母會跑不出來
                current_lst += alphabet
            '''


'''
string的方式
def find_anagrams_helper(s, current_s, ana_lst):
    if len(current_s) == len(s) and current_s not in ana_lst:
        if current_s in read_dictionary():
            print('Found: ' + current_s)
            ana_lst.append(current_s)
            print("Researching...")
    else:
        for i in range(len(s)):
            alphabet = s[i]
            alphanum_in_current_str = current_s.count(alphabet)
            alphanum_in_str = s.count(alphabet)
            if alphanum_in_str > alphanum_in_current_str:
                current_s += alphabet
                if has_prefix(current_s):
                    find_anagrams_helper(s, current_s, ana_lst)
                current_s = current_s[:-1]
'''



def has_prefix(sub_s, dict_set):
    # dict_set 可能會全跑一輪
    """
    :param sub_s: the alphabet combined by helper function
    :return: T or F
    """
    # for dict_word in Dict_lst:
    word = "".join(sub_s)
    for dict_word in dict_set:
        if dict_word.startswith(word):
            return True
    return False


if __name__ == '__main__':
    main()
