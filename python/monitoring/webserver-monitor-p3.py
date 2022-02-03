#!/usr/bin/env python3
from datetime import datetime
import http.client
import os
import re
import smtplib
import socket
import time

import conf

WEB_TIMEOUT = getattr(conf, 'WEB_TIMEOUT', 10)
MAX_ATTEMPTS = 5

socket.setdefaulttimeout(WEB_TIMEOUT)

def get_status_code(host, path="/", attempts=0, ssl=False):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        if ssl:
            context = http.client.ssl.SSLContext()
            conn = http.client.HTTPSConnection(host, context=context)
        else:
            conn = http.client.HTTPConnection(host)
        conn.request("HEAD", path)
        status = conn.getresponse().status
        conn.close()
        if status == 405:
            conn = http.client.HTTPConnection(host)
            conn.request("GET", path)
            status = conn.getresponse().status
            conn.close()
    except socket.timeout as e:
        attempts += 1
        if attempts < MAX_ATTEMPTS:
            # pause then try again
            time.sleep(WEB_TIMEOUT)
            return get_status_code(host, path, attempts, ssl=ssl)
        else:
            return '%s (%s attempts)' % (e, attempts)
    except (Exception, socket.gaierror, socket.error) as e:
        return e
    else:
        return status

def main():
    dead = []
    for u in conf.URLS:
        ssl = False
        if re.match('https://', u) is not None:
            ssl = True
            domain = u.split('/')[2]
            path = '/' + '/'.join(u.split('/')[3:])
        elif re.match('http://', u) is not None:
            domain = u.split('/')[2]
            path = '/' + '/'.join(u.split('/')[3:])
        else: # no protocol given
            domain = u.split('/')[0]
            path = '/' + '/'.join(u.split('/')[1:])
        status = get_status_code(domain, path, ssl=ssl)
        if status not in (200, 
                          #'[Errno -3] Temporary failure in name resolution', 
                          #'[Errno -2] Name or service not known',
                          ):
             dead.append((u, status))

    #with open(os.path.join(conf.LOG_DIR, 'web.log'), 'a+') as f:
    #    f.write('%s %s Status:%s\r\n' % (datetime.now().strftime('%Y-%m-%d %H:%M'), u, status))

    socket.setdefaulttimeout(30)

    if len(dead):
        # ALARM
        msg = "Subject: WEB SERVER DOWN - %s\n" % ', '.join([d[0] for d in dead])
        msg += "\n"
        for d in dead:
            msg += "%s Status: %s\n" % d

        s = smtplib.SMTP(conf.EMAIL_HOST)
        # inform tobi, if wekan is down
        if d[0] == 'https://fb02srv-u103275.wirtschaft.uni-giessen.de/wekan/':
            s.sendmail(conf.FROM_EMAIL,
                       ['tobias.goetz@wirtschaft.uni-giessen.de','tobias@tobias-weiss.org'],
                       msg)
        else:
            s.sendmail(conf.FROM_EMAIL,
                       conf.RECIPIENTS,
                       msg)

if __name__ == '__main__':
    main()
