# ==== twisted/plugins/twist_plugin.py ====
# - Zope modules -
from zope.interface import implements

# - Twisted modules -
from twisted.python import usage
from twisted.application.service import IServiceMaker
from twisted.plugin import IPlugin

# - twist modules -
from twist import twist

class Options(usage.Options):
    synopsis = "[options]"
    longdesc = "Make a twist server."
    optParameters = [
        ['file', 'f', '/etc/users'],
        ['templates', 't', '/usr/share/twist/templates'],
        ['ircnick', 'n', 'twistbot'],
        ['ircserver', None, 'irc.freenode.net'],
        ['pbport', 'p', 8889],
    ]
    
    optFlags = [['ssl', 's']]

class MyServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    
    tapname = "twist"
    description = "twist server."
    options = Options
    
    def makeService(self, config):
        return twist.makeService(config)

serviceMaker = MyServiceMaker()
