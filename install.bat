@echo off
echo Installing ZeroDollarDev - the H-1B killer...
python -m pip install --user crewai playwright continue cursor sweep
playwright install-deps
playwright install
echo.
echo INSTALL COMPLETE
echo.
echo Run the killer swarm now:
python swarm.py
pause
