#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database
MemoRecord = namedtuple("MemoRecord","key, task")

class DBPickler(pickle.Pickler):

    """Docstring for DBPickler. """

    def persistent_id(self, obj):
        """Instead of pickling MemoRecord as a regular class instance, we emit
        a persistend id.

        :obj: TODO
        :returns: TODO

        """
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in our database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not habe a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None

class DBUnpickler(pickle.Unpickler):

    """Docstring for DBUnpickler. """

    def __init__(self, file, connection):
        """TODO: to be defined1. """
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        """This method is invoked whever a persistent ID is encountered.
        Here, pid is the tuple returned py DBPickler

        :pid: TODO
        :returns: TODO

        """
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id,)))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("usupported persistent object")

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    import io
    import pprint

    # Initialize and populate our database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks =(
        'give food to fish',
        'prepare meeting',
        'fight with a zebra'
        )
    for task in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL,?)", (task,))

    # Fetch the records to be pickled
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]
    # Save the records using our custom DBPickler
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    print("Pickled records:")
    pprint.pprint(memos)

    # Update a record, just for good measure.
    cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

    #Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    print("Unpickled records:")
    pprint.pprint(memos)

if __name__ == "__main__":
    main()

