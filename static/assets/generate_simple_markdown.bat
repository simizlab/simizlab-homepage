@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2017-01-19 2017-01-20 2017-01-01 2017-01-31 ^
                        2017-02-23 2017-03-05 2017-03-08 2017-03-24 ^
                        2017-03-27 2017-04-01 2017-06-01 2017-06-23 ^
                        2017-07-03 2017-07-31 2017-09-04 2017-09-12 ^
                        2017-09-19 2017-10-04

::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
