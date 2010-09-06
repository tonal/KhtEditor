#!/usr/bin/python
# -*- coding: utf-8 -*-

#KhtEditor Setup File
import khteditor
import imp

from distutils.core import setup

setup(name='KhtEditor',
      version=khteditor.__version__,
      license='GNU GPLv3',
      description='A source code editor designed for Maemo and Meego devices, support Scripts and Plugins.',
      author='Benoît HERVIER',
      author_email='khertan@khertan.net',
      url='http://www.khertan.net/khteditor',
      depend='pygments',
      packages= ['khteditor', 'khteditor/plugins', 'khteditor/syntax'],
      package_data = {'khteditor': ['icons/*.png'],
                      'khteditor': ['syntax/*.xml']},
      data_files=[('/usr/share/dbus-1/services', ['khteditor.service']),
                  ('/usr/share/applications/hildon/', ['khteditor.desktop']),
                  ('/usr/share/pixmaps', ['khteditor.png'])],
      scripts=['khteditor_launch.py'],
     )

