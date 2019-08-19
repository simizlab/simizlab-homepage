@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2016-01-14 2016-01-20 2016-01-01 2016-02-11 2016-02-22 2016-03-28 ^
                        2016-04-26 2016-04-01 2016-06-24 2016-06-01 2016-07-14 2016-07-23 ^
                        2016-08-01 2016-08-15 2016-09-01 2016-09-16 2016-09-22 2016-11-28 ^
                        2016-10-01 2016-11-01 
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
