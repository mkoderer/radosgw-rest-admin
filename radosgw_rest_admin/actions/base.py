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


class RadosgwRestAdminAction(object):
    def add_arguments(self, subparser):
        # Adds a subparser for the certain command
        raise NotImplementedError()
    
    def request_type(self):
        # request type of the request (get, put, delete...)
        raise NotImplementedError()
        
    def url_base(self):
        # The base url of the request (like admin/user)
        raise NotImplementedError()

    def get_params(self, args):
        # returns a list of parameters for the request
        raise NotImplementedError()
 