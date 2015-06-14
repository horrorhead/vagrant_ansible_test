#!/usr/bin/python2.7
# encoding: utf-8
'''
Verify loadbalancer 
@author:     Mats Cederholm
'''

import sys
import os
import re
import httplib as http

from argparse import ArgumentParser

__all__ = []
__version__ = 0.1
__date__ = '2015-06-14'
__updated__ = '2015-06-14'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

'''Command line options.'''
print(sys.argv)

program_name = os.path.basename(sys.argv[0])
program_version = "v%s" % __version__
program_build_date = str(__updated__)
program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
program_license = '''%s

Created by cederholmm on %s.
http://www.apache.org/licenses/LICENSE-2.0
Distributed on an "AS IS" basis without warranties
or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

try:
    # Setup argument parser
    parser = ArgumentParser(description=program_license)
    parser.add_argument("-n", dest="request_count", action="store", required=True, type=int, help="Number of requests to perform")
    parser.add_argument("-v", dest="verbose", action="store_true", help="set verbosity level [default: %(default)s]")
    parser.add_argument('-V', '--version', action='version', version=program_version_message)
    # Process arguments
    args = parser.parse_args()
    request_count = args.request_count
    verbose = args.verbose

    if verbose:
        print("Verbose mode on")

    response_result = {}

    for x in range(0, request_count):
        conn = http.HTTPConnection("192.168.1.110")
        conn.request("GET", "/")
        resp = conn.getresponse()
        resp_data = resp.read()

        if not resp_data in response_result:
            response_result[resp_data] = 1
        else:
            response_result[resp_data] += 1
    print(response_result)

except Exception as e:
    indent = len(program_name) * " "
    sys.stderr.write(program_name + ": " + repr(e) + "\n")
    sys.stderr.write(indent + "  for help use --help")

