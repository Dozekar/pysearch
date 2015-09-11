# pysearch
python search module

The actual Read Me file for pysearch.
 (The other is a submission test)

Pysearch is a simple python search program.  It searches through just about everything in search of its target.  It makes no attempts to apply transformations to the target, encrypted or otherwise obscured data is not its goal.  It will search through literally any file attempting to find matches including binary files. It's also intended to be as completely cross everything as possible.  Please let me know if any assumptions I've made are interfering with this.  For the sanity of windows users it opens all files it searches in binary mode to prevent damage to any executables.

Notes:

Basic zip file traversal complete, which allows searching of M$ office files.

Most recent fix should have resolve issues with failing to close files on error.
