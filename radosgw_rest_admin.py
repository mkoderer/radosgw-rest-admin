#!/usr/bin/env python

# Copyright 2013 Deutsche Telekom AG
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse
from awsauth import S3Auth
import json
import logging
import os
import requests
import sys
from xml.dom.minidom import parseString


action_classes = {"radosgw_rest_admin.actions.user": ["UserCreate",
                                                      "UserInfo"],
                  "radosgw_rest_admin.actions.bucket": ["BucketLink",
                                                        "BucketInfo"]}
action_objects = []

for action in action_classes:
    module = __import__(action, fromlist=action_classes[action])
    for klass_name in action_classes[action]:
        klass = getattr(module, klass_name)
        action_objects.append(klass())

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='radosgw rest admin')
parser.add_argument('-a', '--aws-key',
                    help="aws key (optional if environment variable "
                    "S3_ACCESS_KEY_ID is set)")
parser.add_argument('-s', '--secret-key', help="secret key (optional "
                    "if environment variable S3_SECRET_ACCESS_KEY is set)")
parser.add_argument('-H', '--host', default='localhost', help="host name "
                    "(fqdn or ip; S3_HOSTNAME can be used instead)")
parser.add_argument('-f', '--format', default='json',
                    help="format (json or xml)")
parser.add_argument('--ssl', action='store_true', help="use ssl")
subparsers = parser.add_subparsers(help='Sub commands', dest='command')


def make_request(args):
    if args.ssl:
        url_prefix = 'https'
    else:
        url_prefix = 'http'

    action = None
    for obj in action_objects:
        if obj.name == args.command:
            action = obj

    params = action.get_params(args)
    params.append("format=%s" % args.format)

    url = '%s://%s/%s?%s' % (url_prefix,
                             args.host,
                             action.url_base(),
                             "&".join(params))

    request_func = getattr(requests, action.request_type())
    response = request_func(url, auth=S3Auth(args.aws_key,
                                             args.secret_key,
                                             args.host))
    if response.status_code >= 200 and response.status_code < 300:
        if response.content is not None or response.content == '':
            if args.format == 'json':
                print(json.dumps(json.loads(response.content),
                                 sort_keys=True,
                                 indent=4,
                                 separators=(',', ': ')
                                 ))
            elif args.format == 'xml':
                xml = parseString(response.content)
                print xml.toprettyxml()
            else:
                print response.content
        sys.exit(0)
    else:
        sys.exit(1)


for action in action_objects:
    action.add_arguments(subparsers)
args = parser.parse_args()

if args.aws_key is None:
    if os.getenv('S3_ACCESS_KEY_ID') is None:
        raise argparse.ArgumentTypeError('aws_key must be defined or '
                                         'S3_ACCESS_KEY_ID must be set')
    args.aws_key = os.environ['S3_ACCESS_KEY_ID']

if args.secret_key is None:
    if os.getenv('S3_SECRET_ACCESS_KEY') is None:
        raise argparse.ArgumentTypeError('secret_key must be defined or '
                                         'S3_SECRET_ACCESS_KEY must be set')
    args.secret_key = os.environ['S3_SECRET_ACCESS_KEY']

if os.getenv('S3_HOSTNAME'):
    args.host = os.environ['S3_HOSTNAME']

make_request(args)
