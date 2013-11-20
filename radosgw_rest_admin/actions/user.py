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

class User(RadosgwRestAdminAction):
    def add_arguments(self, subparser):
        parser = subparser.add_parser(name=self.name)
        parser.add_argument('-u', '--uid', help="User uid")
        parser.add_argument('--display-name', help="Display name")
        parser.add_argument('--subuser', help="Subuser name")
    
    @property
    def request_type(self):
        raise NotImplementedError()
        
    def url_base(self):
        return 'admin/user'

    def get_params(self, args):
        paras = []
        if args.uid:
            paras.append('uid=%s' % args.uid)
        if args.display_name:
            paras.append('display-name=%s' % args.display_name)
        if args.subuser:
            paras.append('subuser=%s' % args.subuser)

        return paras

class UserInfo(User):
    @property
    def name(self):
        return 'user-info'
    
    def request_type(self):
        return 'get'

class UserCreate(User):
    @property
    def name(self):
        return 'user-create'
        
    def request_type(self):
        return 'put'
