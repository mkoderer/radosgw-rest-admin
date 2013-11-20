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
from base import RadosgwRestAdminAction

class Bucket(RadosgwRestAdminAction):
    def add_arguments(self, subparser):
        self.parser = subparser.add_parser(name=self.name)
        self.parser.add_argument('-u', '--uid', help="User uid")
        self.parser.add_argument('--bucket', help="Bucket id")
    
    def url_base(self):
        return 'admin/bucket'

    def get_params(self, args):
        params = []
        if args.uid:
            params.append('uid=%s' % args.uid)
        if args.bucket:
            params.append('bucket=%s' % args.bucket)
        return params

class BucketLink(Bucket):
    @property
    def name(self):
        return 'bucket-link'
    
    def request_type(self):
        return 'put'
    
class BucketInfo(Bucket):
    def add_arguments(self, subparser):
        super(BucketInfo, self).add_arguments(subparser)
        self.parser.add_argument('--stats', action='store_true', 
                                 help="Show statistics")
        
    def get_params(self, args):
        params = super(BucketInfo, self).get_params(args)
        if args.stats:
            params.append('stats=true')
        return params

    @property
    def name(self):
        return 'bucket-info'
    
    def request_type(self):
        return 'get'