@echo off
title GoogleTrend
echo --切换目录
cd /d E:\Dev\Py\GoogleTrendsBatch
echo.
echo --进入虚拟环境
call neco\Scripts\activate
echo.
echo --开始执行脚本
call python trends.py
echo.
echo --退出虚拟环境
call neco\Scripts\deactivate.bat
echo.
echo --脚本执行结束
echo.
pause