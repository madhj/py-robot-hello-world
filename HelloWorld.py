import os, shutil
from operator import attrgetter
import xml.etree.ElementTree as ET

def hello_word():
   print("HELLO WORLD!")

def write_file(filename):
   os.makedirs(os.path.dirname(filename), exist_ok=True)
   f = open(filename, "w")
   f.write("<x></x>")

def verify_file(filename):
   if os.path.isfile(filename):
       print("All ok")
   else:
       raise AssertionError('Expected file to exist')

def match_xml(actual_file_name, expected_file_name):
    xml1 = ET.parse(actual_file_name)
    xml2 = ET.parse(expected_file_name)
    e1 = xml1.getroot()
    e2 = xml2.getroot()
    if elements_equal(e1, e2):
        print("All ok")
    else:
       raise AssertionError('Expected does not match actual')

def elements_equal(e1, e2):
    for node in e1.findall("*"):  # searching top-level nodes only: node1, node2 ...
        node[:] = sorted(node, key=attrgetter("tag"))
    for node in e2.findall("*"): # searching top-level nodes only: node1, node2 ...
        node[:] = sorted(node, key=attrgetter("tag"))
    print(e1.tag, e2.tag)
    if e1.tag != e2.tag: return False
    if e1.text != e2.text: return False
    if e1.tail != e2.tail: return False
    if e1.attrib != e2.attrib: return False
    if len(e1) != len(e2): return False
    return all(elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


def clean_folder(folder):
   shutil.rmtree(folder)
