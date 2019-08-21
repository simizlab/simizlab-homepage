@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2019-01-07 2019-01-16 2019-01-22 2019-02-28 ^
                        2019-03-04 2019-03-08 2019-04-09 2019-04-28 ^
                        2019-05-08 2019-05-10 2019-06-12 2019-06-19 ^
                        2019-07-01
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
