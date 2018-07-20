# 
# Copyright (c) 2018 Intel Corporation 
# 
# SPDX-License-Identifier: Apache-2.0 
#

from openstack_dashboard.api.nova import *

def server_group_create(request, **kwargs):
    return novaclient(request).server_groups.create(**kwargs)