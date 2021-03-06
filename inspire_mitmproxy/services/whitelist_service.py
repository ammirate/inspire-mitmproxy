# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE-MITMROXY.
# Copyright (C) 2018 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Service which allows all requests outside"""
import os

from ..errors import DoNotIntercept
from ..http import MITMRequest, MITMResponse
from ..services.base_service import BaseService


class WhitelistService(BaseService):
    def __init__(self, *args, **kwargs):
        if 'MITM_PROXY_WHITELIST' in os.environ:
            kwargs['hosts_list'] = os.environ['MITM_PROXY_WHITELIST'].split()
        else:
            kwargs['hosts_list'] = kwargs.get('hosts_list', [])

        super().__init__(*args, **kwargs)

    def process_request(self, request: MITMRequest):
        raise DoNotIntercept(self.name, request)

    def process_response(self, request: MITMRequest, response: MITMResponse):
        pass
