@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2014-03-08 2014-04-01 2014-07-01 2014-09-01 2014-11-01
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
