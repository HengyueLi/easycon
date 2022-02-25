#!/usr/bin/env python3
import sys,os,datetime


#--------------
name    = 'easycon'
scripts = ['easycon','easycon.cmd','easycon-cli','easycon-cli.cmd']
#--------------




python   = sys.executable
filepath = os.path.realpath(__file__)
projpath = os.path.dirname(filepath)
dist = os.path.join(projpath,'dist')
passDir = os.path.join(os.environ['DROPBOX_HOME'],'AutoPassword')
sys.path.insert(0, passDir)
import password as pw



setupcontext = '''
import setuptools
#from setuptools import setup

setuptools.setup(
    name='{name}',
    scripts={scripts} ,
    version='{version}',
    author='Hengyue Li',
    author_email='hengyue.li@hengyue.li',
    packages=setuptools.find_packages(),
    license='LICENSE.md',
    description='A tool based on paramiko used to connect to remote server.',
    long_description=open('README.md',encoding="utf8").read(),
    long_description_content_type="text/markdown",
    install_requires={install_requires},
    python_requires='>=3.5',
    url = "https://github.com/HengyueLi/easycon",
)
'''.format(name    = name ,
           scripts = str(scripts),
           version = datetime.datetime.now().strftime("%Y.%m.%d.%H%M") ,
           install_requires = [ i for i in open('requirements.txt').read().split('\n') if len(i)>1  ] )





os.system('rm -rf {}/*'.format(dist))
os.system('rm -rf setup.py')
with open('setup.py','w') as f:
    f.write(setupcontext)
os.system('{} setup.py sdist'.format(python))
#---------------------------------------
# upload with username&password
command = "twine upload dist/* -u {username} -p {password}".format(
                username = pw.GetAutoPasswd('pip','username').get(),
                password = pw.GetAutoPasswd('pip','password').get() )
os.system(command)
#---------------------------------------
os.system('rm -rf dist setup.py *egg-info*')
