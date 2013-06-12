# ==== twisted/plugins/twist_plugin.py ====
'''setup.py for twist.

This is an extension of the Twisted twist tutorial demonstrating how
to package the Twisted application as an installable Python package and
twistd plugin (consider it "Step 12" if you like).

Uses twisted.python.dist.setup() to make this package installable as
a Twisted Application Plugin.

After installation the application should be manageable as a twistd
command.

For example, to start it in the foreground enter:
$ twistd -n twist

To view the options for twist enter:
$ twistd twist --help
'''

__author__ = 'Chris Miles'


import sys

try:
    import twisted
except ImportError:
    raise SystemExit("twisted not found.  Make sure you "
                     "have installed the Twisted core package.")

from distutils.core import setup

def refresh_plugin_cache():
    from twisted.plugin import IPlugin, getPlugins
    list(getPlugins(IPlugin))

setup(
    name="twist",
    version='0.1',
    description="twist server.",
    author_email="you@email.address",
    packages=[
        "twist",
        "twisted.plugins",
    ],
    package_data={
        'twisted': ['plugins/twist_plugin.py'],
    },
    data_files=[
      ('/etc/init.d', ['deb/init.d/twist']),
      ('/etc/twist', ['deb/twist.conf'])
    ])

refresh_plugin_cache()
