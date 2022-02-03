#!/usr/bin/env python
#
# Very basic example of using Python 3 and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# This script is example code from this blog post:
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
# This is an updated version of the original -- modified to work with Python 3.4.
#
import sys
import imaplib
import getpass
import email
import email.header
import datetime
import re
import subprocess
import array
import MySQLdb

M = imaplib.IMAP4('www.tobias-weiss.org')
EMAIL_ACCOUNT = "tobias@tobias-weiss.org"
EMAIL_FOLDER = "INBOX/HIWI/unsubscribe"

HOST = "localhost"
USER = "root"
DB_PASS = ""
DB = "bounce"
db= MySQLdb.connect(HOST, USER, DB_PASS, DB)

def process_mailbox(M):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    rv, data = M.search(None, 'TO', 'wiwilab@uni-jena.de')
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        p = re.compile(r"Undelivered Mail Returned to Sender")
        m = p.search(subject)
        if m:
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    p = re.compile(r"<.*@.*>: Recipient address rejected")
                    m = p.search(part.get_payload())
                    if m:
                        address = m.group()
                        address = address[1:-29]
                        if not address in address_list:
                            address_list.append(address)
    for address in address_list:
        cursor=db.cursor()
        sql = "INSERT INTO mails (mail, comment) VALUES ('{}', '{}')".format(address, address)
        print(sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        db.close()

if __name__ == "__main__":
    try:
        rv, data = M.login('tobias', getpass.getpass())
    except imaplib.IMAP4.error:
        print ("LOGIN FAILED!!! ")
        sys.exit(1)

#  list maibox folders
# rv, mailboxes = M.list()
# if rv == 'OK':
        # print("Mailboxes:")
        # print(mailboxes)

    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print("Processing bouce mails...\n")
        address_list = []
        process_mailbox(M)
        M.close()
    else:
        print("ERROR: Unable to open mailbox ", rv)

    M.logout()
