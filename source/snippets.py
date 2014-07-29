#!/usr/bin/python
# encoding: utf-8
from __future__ import unicode_literals

import re
import os
import sys
import subprocess
from workflow import Workflow

PREFIX = ',,'

def to_unicode(obj, encoding='utf-8'):
    """Ensure passed text is Unicode"""
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

def get_clipboard():
    """Retrieve data from clipboard"""

    os.environ['__CF_USER_TEXT_ENCODING'] = "0x1F5:0x8000100:0x8000100"
    proc = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    return to_unicode(stdout)


##################################################
### Expand In-Text Snippets Functions
##################################################

def _split_set(item, delim):
    """Split multi-line snippet dictionaries"""
    if delim in item:
        split = filter(None, item.split(delim))
        return split
    else:
        return item

def _snippet_dict(item, delim):
    """Create Python snippet dictionary"""
    _dict = {}
    if delim in item:
        sub_l = _split_set(item, delim)
        for sub in sub_l:
            [key, val] = sub.split(':')
            _dict[key.strip()] = val.lstrip()
    return _dict

def expand_snippets(the_str):
    """Find, Expand, and Replace any in-text snippets"""
    _snippets = re.findall(r"\^{3}(.*?)\^{3}", the_str, flags=re.S)

    _dict = {}
    for i in _snippets:
        if '\r' in i: 
            # If multi-line with ``carriage return``
            _dict.update(_snippet_dict(i, '\r'))
        elif '\n' in i:
            # If multi-line with ``newline``
            _dict.update(_snippet_dict(i, '\n'))
        else:
            # If single line
            [key, val] = i.split(':')
            _dict[key.strip()] = val.lstrip()

    # Find and replace all snippets with expanded text
    for key in sorted(_dict, key=len, reverse=True):
        new_key = PREFIX + key
        the_str = the_str.replace(new_key, _dict[key])
    
    # Remove all snippet dictionaries from text
    the_str = re.sub(r"\^{3}(.*?)\^{3}", "", the_str, flags=re.S)
    return the_str


def get_input(wf):
    """Get text input from Alfred"""
    if wf.args[0] == '':
        # Get input text from clipboard
        the_str = get_clipboard()
    else:
        the_str = wf.args[0]
    return to_unicode(the_str)

def main(wf):
    # Get input text
    _str = get_input(wf)
    #_str = get_clipboard()
    clean_str = expand_snippets(_str)
    print clean_str.encode('utf-8')

if __name__ == '__main__':
    WF = Workflow()
    sys.exit(WF.run(main))
