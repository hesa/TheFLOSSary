import os
import re
import time
import sys
import signal
from subprocess import Popen
from threading import Thread
from subprocess import PIPE
import subprocess

class CommandRunner( Thread ):
   def __init__ (self, Cmd):
      Thread.__init__(self)
      self.mCmd = Cmd
      self.mOutput = ()
      self.mPid = -1
      self.mReturnCode = -1
      self.mError =()

   def run(self):
      p = Popen ( self.mCmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      self.mPid = p.pid
      self.mOutput, self.mError = p.communicate()
      self.mReturnCode = p.returncode

   def output(self):
      return self.mOutput, self.mError

   def terminate( self ):
      if self.mPid != -1:
         os.kill( self.mPid, signal.SIGTERM )
         if self.mPid == True:
            self.join(5)
            os.kill( self.mPid, signal.SIGKILL )
      self.mPid = -1


def RunCommand( Cmd, TimeOutSeconds=-1 ):
   runner = CommandRunner ( Cmd )
   runner.start()
   if TimeOutSeconds == -1:
       runner.join()
   else:
       runner.join( TimeOutSeconds )
   if runner.isAlive():
       runner.terminate()
       runner.join( 5 )
       return ( runner.mReturnCode, runner.output(), True )
   else:
       return ( runner.mReturnCode, runner.output(), False )

def run_or_die( cmd, errormessage ):
	runner = RunCommand( cmd )
	if runner[0] != 0:
		details = ' '.join( cmd )
		raise Exception( 'Unable to call {0}: {1}'.format( details, errormessage ) )
	return runner[1]
