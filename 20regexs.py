import re

nospace = re.compile(r"[\S]+")
quotation = re.compile(r"\"[^\s][^\"]*[^\s]\"")
twonum = re.compile(r"(\-?\d+(?:\.\d+)?)(?:(?:\, )|(?:\,)|(?: ))(\-?\d+(?:\.\d+)?)")
likely_name = re.compile(r"[A-Z](?:[a-z]+|\.) (?:[A-Z](?:[a-z]+|\.) )?[A-Z][a-z]+")
