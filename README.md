# FreeNAS-rsync-helper

This is a tool which allows you to brows to a directory to copy and then past locally on the host.

Originally this was built to be used on a FreeNAS system so that I couold copy and past between datasets
without having to go through the network. Instead this script transferes at local disk speed.

Currenty features are:
- Use copy, move, or rsync to work with files
- Defaults to preserving file permissions and verbose printing
- Steps through the directories starting at the "initial_dir" on line 4 which can be modified to suit your need
- Can work with either the directory itself or just the files in the directory. Example: transfer files into another directory or move the directory itself to another location.