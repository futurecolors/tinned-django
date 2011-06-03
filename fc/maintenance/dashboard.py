# -*- coding: utf-8 -*-
from admin_tools.dashboard import modules
from models import Config

class Maintenance(modules.DashboardModule):
    template = 'maintenance/dashboard_block.html'

    def is_empty(self):
        return False

    def __init__(self, **kwargs):
        super(Maintenance, self).__init__(**kwargs)

    def init_with_context(self, context):
        self.in_maintenance_mode = Config.is_maintenance()
        if 'maintenance' in context['request'].POST:
            self.in_maintenance_mode = not self.in_maintenance_mode
            Config.set_maintenance_state(self.in_maintenance_mode)