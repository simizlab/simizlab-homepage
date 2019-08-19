@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2018-02-22 2018-03-02 2018-03-05 2018-03-19 ^
                        2018-05-14 2018-06-21 2018-06-25 2018-08-03 ^
                        2018-08-22 2018-09-16 2018-10-23 2018-11-01 ^
                        2018-11-07 2018-11-12
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
