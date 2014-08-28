# -*- coding: utf-8

import sys
import qgis.utils

print 'start'

_out = sys.stdout

def installOutputBuffer():
  """Attach stdout and stderr to a variable, allowing for
  CGI style server plugins: to produce an output a plugin
  just have to print out something on stdout or stderr
  TODO: use an efficient cStringIO instead of a plain str
  """
  class CaptureOutErr:
    def __init__(self):
      self.value = ''
    def write(self, txt):
      self.value += txt
    def __unicode__(self):
      ret = self.value
      self.value = ''
      return ret
    def __str__(self):
      ret = self.value
      self.value = ''
      return unicode(ret).encode('utf-8')
  outputBuffer = CaptureOutErr()
  sys.stdout = outputBuffer
  #sys.stderr = outputBuffer
  return outputBuffer

buf = installOutputBuffer()

print "Call n°"

sys.stdout = _out
print buf.value


