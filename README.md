# Log-File-Anylizer-Practice
This analyze log files and give a practical summary that can be used.

##Sample Input:

server.log:
2024-06-01 08:00:01 INFO Server started
2024-06-01 08:01:12 INFO User login successful
2024-06-01 08:02:45 WARNING High memory usage detected
2024-06-01 08:03:10 INFO User requested dashboard
2024-06-01 08:05:32 ERROR Database connection failed
2024-06-01 08:05:35 ERROR Database connection failed
2024-06-01 08:06:00 INFO Retrying database connection
2024-06-01 08:07:18 INFO Database connection restored
2024-06-01 08:10:50 WARNING Disk space low
2024-06-01 08:12:30 INFO User logged out

##Sample Output:
====== LOG SUMMARY ======
Total entries: 10

INFO:     6
WARNING:  2
ERROR:    2

Most common ERROR:
"Database connection failed" (2 times)
========================
