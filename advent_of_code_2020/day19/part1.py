#!/usr/bin/env python3


def parse_input():
    with open("test2", "r") as f:
        text = f.read()
    rules, messages = text.split("\n\n")
    rules_dict = {}
    rules = rules.replace('"', "").split("\n")
    messages = messages.split("\n")
    for line in rules:
        key, possib = line.split(": ")
        possib = possib.split(" | ")
        rules_dict[key] = possib
    return rules_dict, messages


def translate_dict(rules_dict, translated, needs):
    newly_translated = []
    for key2 in needs.keys():
        if needs[key2] - set(translated.keys()) == set({}):
            newly_translated.append(key2)
            translated[key2] = set({})
            for word in rules_dict[key2]:
                split = word.split(" ")
                if len(split) < 2:
                    translated[key2] = translated[key2].union(
                        translated[split[0]])
                else:
                    item1, item2 = split
                    translated[key2] = translated[key2].union(
                        [a + b for a in translated[item1] for b in translated[item2]])

    for key in newly_translated:
        del rules_dict[key]
        del needs[key]

    if '0' not in translated.keys():
        rules_dict, translated, needs = translate_dict(
            rules_dict, translated, needs)
    return(rules_dict, translated, needs)


def get_translated_and_needs(rules_dict):
    translated = {}
    needs = {}
    for key in rules_dict.keys():
        if all_string(rules_dict[key]):
            translated[key] = set(rules_dict[key])
        else:
            needs[key] = set([item for word in rules_dict[key]
                              for item in word.split(" ")])
    return(translated, needs)


def all_string(list1):
    for elem in list1:
        if not elem.isalpha():
            return False
    return True


if __name__ == "__main__":
    rules_dict, messages = parse_input()
    translated, needs = get_translated_and_needs(rules_dict)

    (rules_dict, translated, needs) = translate_dict(
        rules_dict, translated, needs)
    print(translated)
    print(sum([1 for message in messages if message in translated['0']]))
