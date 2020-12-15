Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "M:\Programs\workspace\bat_vbs_py\test.bat" & Chr(34), 0
Set WshShell = Nothing