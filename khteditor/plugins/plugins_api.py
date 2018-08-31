from __future__ import print_function

import sys
import os
import glob
#from PyQt4.QtCore import QSettings

PATHS = [os.path.join(os.path.dirname(os.path.abspath(__file__)) ),
         os.path.join(os.path.dirname(sys.argv[0]),'plugins'),
         os.path.join(os.path.expanduser("~"),'.khteditor','plugins'),
         os.path.join(os.path.abspath(sys.path[0]),'plugins')]

class Plugin(object):
    capabilities = []
    __version__ = '0.5'

    def __repr__(self):
        return '<%s %r>' % (
            self.__class__.__name__,
            self.capabilities
        )

    #beforeCursorPositionChanged capabilities
    def do_beforeCursorPositionChanged(self,widget):
        """Called before cursor position change"""
        raise NotImplementedError

    #afterKeyPressEvent capabilities
    def do_afterKeyPressEvent(self,widget,event):
        """Called after a key pressed event"""
        raise NotImplementedError

    #beforeKeyPressEvent capabilities
    def do_beforeKeyPressEvent(self,widget,event):
        """Called before a key pressed event"""
        raise NotImplementedError

    #afterFileSave capabilities
    def do_afterFileSave(self,widget,event):
        """Called after file save"""
        raise NotImplementedError

    #afterFileOpen capabilities
    def do_afterFileOpen(self,widget,event):
        """Called after opening a file"""
        raise NotImplementedError

    #beforeFileSave capabilities
    def do_beforeFileSave(self,widget,event):
        """Called after file save"""
        raise NotImplementedError

    #toolbarHook capabilities
    def do_toolbarHook(self,menu):
        """Called while initializing the toolbar for adding
           qaction from plugins to plugin menu"""
        raise NotImplementedError


def filter_plugins_by_capability(capability,plugins_list):
    result = []
    for plugin in plugins_list:
        if capability in plugin.capabilities:
            result.append(plugin)
    return result

def get_plugins_by_capability(capability):
    result = []
    for plugin in Plugin.__subclasses__():
        if capability in plugin.capabilities:
            result.append(plugin)
    return result

def load_plugins(plugins):
    for plugin in plugins:
        try:
            #Get the module path for loading plugin path
            md_path = __name__.split('.')[:-1]
            print(__import__('%s.%s' % ('.'.join(md_path),plugin), None, None, ['']))
        except Exception as err:
            print('Failed to load : %s : %s' % (str(plugin), str(err)))  #Probably defect plugin

def discover_plugin_in_paths():
    plugins = []
    for path in PATHS:
        for plug_path in glob.glob(os.path.join(path,'*.py')):
            plugin_name = os.path.splitext(os.path.basename(plug_path))[0]
            if not (plugin_name in plugins):
                print('Discover plugin : ' + plugin_name)
                plugins.append(plugin_name)
    return plugins

def init_plugin_system():
    print('Init plugin system --')

    #Add path to sys.path
    for path in PATHS:
        if not path in sys.path:
            sys.path.insert(1, path)
            print('added to sys path',path)

    #Discover plugins in path
    plugins = discover_plugin_in_paths()
    try:
        plugins.remove('plugins_api')
        plugins.remove('__init__')
    except:
        pass

    #Load plugins
    load_plugins(plugins)

def find_plugins():
    return Plugin.__subclasses__()

if __name__ == '__main__':
    discover_plugin_in_paths()
