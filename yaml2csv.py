#!/usr/bin/python2.7
import sys
import csv
import yaml
import codecs

TO_BE_TRANSLATED_MARK = "***TO BE TRANSLATED***"

def collect(result, node, prefix=None):
    for key,value in node.items():
        new_prefix = (key if prefix == None else prefix + "." + key)
        if isinstance(value, dict):
            collect(result, value, new_prefix)
        else: 
            result[new_prefix] = value

def collect_old_csv(filename):
    result = {}
    reader = csv.reader(open(filename))
    for row in reader:
        if TO_BE_TRANSLATED_MARK not in row[1]:
            result[row[0]] = row[1].decode("utf-8")
    return result

def flatten(namespace=None,old_csv=None):
    namespace = "" if namespace == None else namespace + "."

    en_src = yaml.load(open("%sen.yml" % namespace))
    ja_src = yaml.load(open("%sja.yml" % namespace))

    en = {}
    collect(en, en_src["en"])
    ja = {}
    collect(ja, ja_src["ja"])

    ja_old = collect_old_csv(old_csv) if old_csv else {}

    writer = csv.writer(sys.stdout)
    for key,value in sorted(en.items()):
        val = TO_BE_TRANSLATED_MARK + value
        if key in ja: val = ja[key]
        elif key in ja_old: val = ja_old[key]
        writer.writerow([key, val.encode("UTF-8")])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: yaml2csv.py namespace('server'|'client') [old-translated-csv-file]"
        sys.exit(1)

    flatten(sys.argv[1], None if len(sys.argv) < 3 else sys.argv[2])
