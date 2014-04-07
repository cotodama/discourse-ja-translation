#!/usr/bin/python2.7
import sys
import collections
import csv
import yaml

class literal_unicode(unicode): pass

def literal_unicode_representer(dumper, data):
    return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def spread(node, path, value):
    if value.startswith("***TO BE TRANSLATED***"): return
    next_name = path[0]
    if len(path) == 1:
        node[next_name] = value
        return
    if next_name not in node:
        node[next_name] = {}
    spread(node[next_name], path[1:], value)

def entree(filename):
    reader = csv.reader(open(filename))
    root_node = { "ja": {} }
    for row in reader:
        value = row[1] if is_ascii(row[1]) else row[1].decode("utf-8")
        spread(root_node["ja"], row[0].split('.'),literal_unicode(value) if '\n' in value else value)
    yaml.dump(root_node, sys.stdout,allow_unicode=True,width=100000,default_flow_style=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: csv2yaml.py input_csv_file_name"
        sys.exit(1)

    yaml.add_representer(literal_unicode, literal_unicode_representer)

    entree(sys.argv[1])
