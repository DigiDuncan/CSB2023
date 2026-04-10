@echo off
echo Press [ENTER] to delete ALL RPYC FILES!
pause
for /R %~dp0 %%f in (*.rpyc) do (
	echo Deleting %%f...
	del %%f
)
echo Done!
pause