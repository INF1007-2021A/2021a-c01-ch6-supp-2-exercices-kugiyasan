#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools

from typing import Dict, List, Set


def get_even_keys(dictionary: Dict[int, str]) -> Set[int]:
    return {key for key in dictionary if key % 2 == 0}


def join_dictionaries(dictionaries: List[Dict[int, str]]) -> Dict[int, str]:
    d1 = dictionaries[0]
    d2 = dictionaries[1]
    d1.update(d2)
    return d1


def dictionary_from_lists(keys: List[str], values: List[str]) -> Dict[str, str]:
    return {key: values[i] for i, key in enumerate(keys)}


def get_greatest_values(dictionary: Dict[str, int], num_values: int) -> List[int]:
    return sorted(dictionary.values(), reverse=True)[:num_values]


def get_sum_values_from_key(dictionaries: List[Dict[str, int]], key: str) -> int:
    return sum(d[key] for d in dictionaries if key in d)


if __name__ == "__main__":
    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    print(get_even_keys(yeet))
    print()

    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    doot = {0xBEEF: "doot", 0xDEAD: "DOOT", 0xBABE: "dOoT"}
    print(join_dictionaries([yeet, doot]))
    print()

    doh = ["D'OH!", "d'oh", "DOH!"]
    nice = ["NICE!", "nice", "nIcE", "NAIIIIICE!"]
    print(dictionary_from_lists(doh, nice))
    print()

    nums = {"nice": 69, "nice bro": 69420, "AGH!": 9000, "dude": 420, "git gud": 1337}
    print(get_greatest_values(nums, 1))
    print(get_greatest_values(nums, 3))
    print()

    bro1 = {"money": 12, "problems": 14, "trivago": 1}
    bro2 = {"money": 56, "problems": 406}
    bro3 = {"money": 1, "chichis": 1, "power-level": 9000}
    print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
    print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
    print()
