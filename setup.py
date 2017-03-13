from distutils.core import setup
import py2exe

setup(options={"py2exe":{"includes":["sip"], 'bundle_files': 1, 'optimize':2, 'dll_excludes':['crypt32.dll', 'mpr.dll'],'compressed': True}, },
      windows=[
          {
              "script": "SubFinder.py",
              "icon_resources": [(0, "goldfish.ico")],
              "dest_base": "SubFinder"
          }
      ],
      zipfile= None
      )
