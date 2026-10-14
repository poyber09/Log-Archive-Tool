#log-archive-tool

A small Python CLI that archives a directory of log files into a timestamped `.tar.gz` bundle and optionally extracts it back.

Built as part of the [roadmap.sh log-archive-tool project](https://roadmap.sh/projects/log-archive-tool)

##Features
- Compresses any log directory into `~/system_log_archive/logs_archive_<timestamp>.tar.gz`
- Timestamped filenames (`YYYYMMDD_HHMMSS`) so archives never collide
- Optional `--decompress` flag to extract the archive right after creating it
- Validates the input path and exits with a non-zero code on error

##Usage

Archive a log directory:
	./log-archive.py /var/log

Archive and immediately extract:
	./log-archive.py /var/log --decompress

Show help:
	./log-archive.py --help
