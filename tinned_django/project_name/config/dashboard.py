# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import Dashboard, modules
from admin_tools.menu import Menu, items
from admin_tools.utils import get_admin_site_name


MODELS = []
#MODELS = [(u'Section name', ['apps.aaa.models.ModelName',
#                             'apps.bbb.models.Content',
#                            ]),
#]


class AdminIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.append_applications()
        self.append_quick_links(context)

    class Media:
        css = ()

    def append_quick_links(self, context):
        site_name = get_admin_site_name(context)
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))

    def append_applications(self):
        for title, models in MODELS:
            self.children.append(modules.AppList(title, models=models))


class AdminMenu(Menu):
    def __init__(self, **kwargs):
        super(AdminMenu, self).__init__(**kwargs)
        self.children += [self.link_to_home(),
                          self.bookmarks(),
                          self.link_to_site()]

    def link_to_home(self):
        return items.MenuItem(_('Dashboard'), reverse('admin:index'))

    def applist(self):
        return items.AppList(_('Applications'))

    def bookmarks(self):
        return items.Bookmarks(_('Bookmarks'))

    def link_to_site(self):
        return items.MenuItem('Back to site', '/')
