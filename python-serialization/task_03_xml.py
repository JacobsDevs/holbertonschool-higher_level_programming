#!/usr/bin/python3
"""
Module containing the serialize and deserialize functions for xml.
"""
import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    """Serializes the provided dictionary in xml

    Args:
    @dictionary: The dict to serialize.
    @filename: The file to write the tree to.
    """

    parent = ET.Element('data')
    for k, v in dictionary.items():
        child = ET.Element(k)
        child.text = str(v)
        parent.append(child)
    ptree = ET.ElementTree(parent)
    ptree.write(filename)

def deserialize_from_xml(filename):
    """Deserializes the provided xml file to a dictionary

    Args:
    @filename: The file to read the tree from
    
    Return:
    Dictionary representation of the XML file.
    """
    tree = ET.parse(filename)
    my_obj = {}
    for i in tree.getroot():
        my_obj[i.tag] = i.text
    return my_obj
