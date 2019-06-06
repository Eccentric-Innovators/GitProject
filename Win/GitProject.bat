@echo off
mkdir %1
cd %1
git init
IF %2.==. GOTO No2
python %~dp0start_git_repo.py %1 %2 %~dp0
GOTO END

:No2
python %~dp0start_git_repo.py %1 getip %~dp0

:END