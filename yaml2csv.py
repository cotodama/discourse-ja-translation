#!/usr/bin/python2.7
import sys
import collections
import csv
import yaml

def collect(result, node, prefix=None):
    for key,value in node.items():
        new_prefix = (key if prefix == None else prefix + "." + key)
        if isinstance(value, dict):
            collect(result, value, new_prefix)
        else: 
            result[new_prefix] = value

def flatten(namespace=None):
    namespace = "" if namespace == None else namespace + "."

    en_src = yaml.load(open("%sen.yml" % namespace))
    ja_src = yaml.load(open("%sja.yml" % namespace))

    en = collections.OrderedDict()
    collect(en, en_src["en"])
    ja = collections.OrderedDict()
    collect(ja, ja_src["ja"])

    writer = csv.writer(sys.stdout)
    for key,value in en.items():
        writer.writerow([key, (ja[key] if key in ja else "***TO BE TRANSLATED***" + value).encode("UTF-8")])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: csv2yaml.py namespace('server'|'client')"
        sys.exit(1)

    flatten(sys.argv[1])
