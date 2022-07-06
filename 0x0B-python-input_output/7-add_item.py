#!/usr/bin/python3
"""7-add_item module"""
import sys


saving = __import__('5-save_to_json_file').save_to_json_file
loading = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
file_save = []

try:
    loading(file)
except FileNotFoundError:
    file_save = []

file_save.extend(sys.argv[1:])
saving(file_save, file)
