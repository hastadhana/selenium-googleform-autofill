
@echo off
cmd /k "cd /d fill-env\Scripts & activate & cd /d    ..\.. & python fill.py & cd /d fill-env\Scripts & deactivate"
pause