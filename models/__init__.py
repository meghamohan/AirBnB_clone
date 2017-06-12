#!/usr/bin/python3
""" Module for init"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
