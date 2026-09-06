@echo off
echo Stopping ViHok AI servers...
taskkill /FI "WindowTitle eq ViHok Backend*" /T /F
taskkill /FI "WindowTitle eq ViHok Frontend*" /T /F
echo Stopped!
pause
