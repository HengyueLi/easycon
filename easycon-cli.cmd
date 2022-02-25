::# do not print everything on screen ::
@echo off
::# project path ::
set dir=%~dp0
::# python script ::
set pyscpt=%dir%easycon-cli
::#run script by python in env. Args are passed::
python %pyscpt% %*
