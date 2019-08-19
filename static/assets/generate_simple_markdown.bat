@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2015-01-13 2015-04-01 2015-06-24 2015-09-08 2015-10-01 2015-10-05 2015-11-01
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
