## Copyright (C) 2007-2010 Red Hat, Inc., Ben Turner <bturner@redhat.com>

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools

class iscsitarget(sos.plugintools.PluginBase):
    """iscsi-target related information
    """

    def checkenabled(self):
        self.packages = [ "scsi-target-utils" ]
        return sos.plugintools.PluginBase.checkenabled(self)

    def setup(self):
        self.addCopySpec("/etc/tgt/targets.conf")
        self.collectExtOutput("tgtadm --lld iscsi --op show --mode target")
