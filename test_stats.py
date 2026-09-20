import pytest
from stats import count_words, count_characters, sort_on, chars_dict_to_sorted_list

#Testing: Expected input, No input, Number, Dictionary, List, Weird stuff

def test_count_words():
    assert count_words("hello there") == 2
    assert count_words("") == 0
    with pytest.raises(Exception):
        count_words(104213) #Random number 
    with pytest.raises(Exception):
        count_words({})
    with pytest.raises(Exception):
        count_words([])
    assert count_words("(o゜▽゜)o☆         ♪(´▽｀)") == 2 #Ensuring spaces and special characters don't affect it
    #(The two "o"s are the characters)
    assert count_words("😁 😂") == 2 #Emojis separated by a space are treated as separate words


def test_count_characters():
    assert count_characters("HI") == {'h': 1, 'i': 1}
    assert count_characters("") == {}
    with pytest.raises(Exception): #Expected to crash hence is an exception 
        count_characters(12098753) #More random numbers!!
    with pytest.raises(Exception):
        count_characters({})
    with pytest.raises(Exception):
        count_characters([])
    assert count_characters("^_____^") == {'^': 2, '_': 5}
    assert count_characters("寫中文") == {'寫': 1, '中': 1, '文': 1} #不是英文!


def test_sort_on():
    assert sort_on(["h", 1]) == 1
    assert sort_on(["i", 1]) == 1
    assert sort_on(["", None]) == 0 #The function "sort_on" uses an if statement to check 
    with pytest.raises(Exception):
        sort_on(7230921)
    with pytest.raises(Exception):
        sort_on({})
    with pytest.raises(Exception):
        sort_on([])


def test_chars_dict_to_sorted_list():
    assert chars_dict_to_sorted_list({'h': 1}) == [('h', 1)]
    assert chars_dict_to_sorted_list({'a': 5, 'c': 12, 'b': 2}) == [('c', 12), ('a', 5), ('b', 2)] #Ensuring highest count comes first
    assert chars_dict_to_sorted_list({}) == []  
    assert chars_dict_to_sorted_list([]) == []  #It returns [] instead of crashing! ( ﾉ ﾟｰﾟ)ﾉ     
    #Apparently dictionaries and lists can both be looped over using "for"!
    with pytest.raises(Exception):
        chars_dict_to_sorted_list(1029832)
    assert chars_dict_to_sorted_list({'b': 2, 'a': 2}) == [('b', 2), ('a', 2)] #The program keeps the insertion order if the value is the same - [('a', 2), ('b', 2)] fails!
