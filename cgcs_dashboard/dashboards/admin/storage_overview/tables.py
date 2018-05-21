# Copyright (c) 2016 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use
# of this software may be licensed only pursuant to the terms
# of an applicable Wind River license agreement.
#
from django.utils.translation import ugettext_lazy as _
from horizon import tables


class UsageTable(tables.DataTable):
    service = tables.Column('service_name', verbose_name=_('Service name'))
    backend = tables.Column('backend_name', verbose_name=_('Backend name'))
    capacity = \
        tables.Column('total_capacity', verbose_name=_('Total Capacity (GiB)'))
    free = \
        tables.Column('free_capacity', verbose_name=_('Free Capacity (GiB)'))

    class Meta(object):
        name = "usage"
        hidden_title = False
        verbose_name = _("Storage Services and Backends Usage")
        multi_select = False

    def get_object_id(self, datum):
        return datum


class MonitorsTable(tables.DataTable):
    host = tables.Column('host',
                         verbose_name=_('Host'))
    rank = tables.Column('rank',
                         verbose_name=_('Rank'))

    def get_object_id(self, obj):
        return obj.host  # hostname is always unique

    class Meta(object):
        name = "monitors"
        verbose_name = _("Monitors")
        multi_select = False


class OSDsTable(tables.DataTable):
    host = tables.Column('host',
                         verbose_name=_('Host'))
    name = tables.Column('name',
                         verbose_name=_('Name'))
    status = tables.Column('status',
                           verbose_name=_('Status'))

    def get_object_id(self, obj):
        return obj.id

    class Meta(object):
        name = "osds"
        verbose_name = _("OSDs")
        multi_select = False
