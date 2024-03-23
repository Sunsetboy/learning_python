"""
Every time you write data to this file, you use the Write method like write(“hello world”), 
but if you have enough buffer in memory (buffer_size), you write to buffer first. 
Only write to disk when the buffer is full (using the flush method to write to disk).
Implement both the Write and flush functions
"""

class File:
    def write(self, bytes: bytearray):
        pass

class BufferedFile(File):
    def __init__(self, f: File, buffer_size: int):
        pass
    def write(self, bytes: bytearray):
        print("write", bytes)
    def flush(self):
        print("flushing to disk")