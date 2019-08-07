import sys, os, os.path
def reverse_readline(filename, my_name, buf_size=8192):
    with open(filename) as fh:
        segment = None
        Found = False
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0 and Found == False:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # The first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read

            if segment is not None:
                # If the previous chunk starts right from the beginning of line
                # do not concat the segment to the last line of new chunk.
                # Instead, yield the segment first 
                if buffer[-1] != '\n':
                    lines[-1] += segment
                else:
                    print(segment, '26')

            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if lines[index] and '#' in lines[index] and my_name not in lines[index]:
                    line = lines[index].split()
                    for i in line:
                        if '#' in i:
                            print(i[7:])
                            Found = True
                            break
                if Found:
                    break
my_name = 'bi'
default_path = 'C:\\Program Files (x86)\\Hearthstone\\Logs\\Power_old.log'

if not os.path.exists(default_path):
    print('You have to have the game running and play a match for log file to appear.')
    sys.exit(-1)

reverse_readline(default_path, my_name)
