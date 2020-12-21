#!/usr/bin/env python3


def parse_input():
    with open("input", "r") as f:
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

    if '0' not in translated.keys() or '42' not in translated.keys() or '31' not in translated.keys():
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
    rules_dict['8'] = ['oit']
    rules_dict['11'] = ['onz']
    translated, needs = get_translated_and_needs(rules_dict)

    (rules_dict, translated, needs) = translate_dict(
        rules_dict, translated, needs)
    print("42", translated['42'])
    print("31", translated['31'])
    print("0", translated['0'])
    matches0 = 0
    i = len(list(translated['42'])[0])

    # hard coding matches for rules 8 and 11
    for message in messages:
        matches11 = False
        matches8 = False
        while message[-i:] in translated['31'] and message[:i] in translated['42']:
            message = message[i:-i]
            matches11 = True
        if matches11:
            while message[:i] in translated['42']:
                message = message[i:]
                matches8 = True
            if matches8 and len(message) == 0:
                matches0 += 1
    print(matches0)

    rules_dict['8'] = ['42', '42 8']
    rules_dict['11'] = ['42 31', '42 11 31']
