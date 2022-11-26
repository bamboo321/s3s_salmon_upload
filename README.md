# s3s_salmon_upload

This program uploads multiple json files saved with the -o option of s3s to stat.ink.

## usage
1. Copy `export_upload.py` to s3s dir.
```Bash
$ pwd
/home/user/s3s

$ ls -l
合計 276
-rw-rw-r--    1 user user 34916  9月 11 19:10 LICENSE.md
-rw-r--r--    1 user user  9886 11月 26 03:55 README.md
-rw-r--r--    1 user user  1559 11月 27 02:21 config.txt
-rw-rw-r--    1 user user  1089 11月 26 19:36 export_upload.py
-rw-r--r--    1 user user 15510 11月 26 12:55 iksm.py
-rw-r--r--    1 user user    56 11月 24 09:55 requirements.txt
-rwxr-xr-x    1 user user 66775 11月 26 21:44 s3s.py
-rw-r--r--    1 user user  6523 11月 26 03:55 utils.py
```

2. Create a directory named exports and copy the `export-(unix_time)` directory output from s3s into it
```Bash
$ mkdir exports
$ ls -lt exports/ | head
合計 0
drwxr-xr-x 2 user user 72 11月 27 02:01 export-1669482114
drwxr-xr-x 2 user user 72 11月 27 01:02 export-1669478532
drwxr-xr-x 2 user user 72 11月 27 00:02 export-1669474923
drwxr-xr-x 2 user user 72 11月 26 23:02 export-1669471349
drwxr-xr-x 2 user user 72 11月 26 22:02 export-1669467727
drwxr-xr-x 2 user user 72 11月 26 21:02 export-1669464124
drwxr-xr-x 2 user user 72 11月 26 20:01 export-1669460518
drwxr-xr-x 2 user user 72 11月 26 19:02 export-1669456923
drwxr-xr-x 2 user user 72 11月 26 18:01 export-1669453315
```

3. Execute
```Bash
$ python3 export_upload.py
```