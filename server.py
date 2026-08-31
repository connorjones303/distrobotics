# echo server
import socket
import datetime
from pathlib import Path

host = ''
port = 40001
clips_folder = './clips'

def format_clip_filename():
    # 1. Get the current date and time from the system clock
    now = datetime.now()
    # 2. Format it: YYYYMMDD_HHMMSS
    # %Y = 4-digit year, %m = 2-digit month, %d = 2-digit day
    # %H = 24-hour, %M = minute, %S = second
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    # 3. Combine into a clean filename string
    return f"clip_{timestamp}.mp4"

def handle_command(command) -> str:
    return_string = ''
    keyword_args = command.split(); 
    primary_command = keyword_args[0]
    if primary_command == 'clip':
        if len(keyword_args) > 1:
            # flag parsing
            flags = list(keyword_args[1])
            if 'r' in flags:
                return_string += 'initializing recording clip\n'
                return return_string
            if 's' in flags:
                if len(keyword_args) == 3:
                    clip_name = keyword_args[2]
                    clip_path = Path(clips_folder, clip_name)
                    if clip_path.exists():
                        return_string += f'sending clip {clip_name}\n'
                        return return_string
                    else:
                        return_string = f'error path not found: {clip_path}'
                        return return_string
                else:
                    return_string = 'sending most recent clip\n'
                    return return_string
        else:
            # default 'clip' command
            return_string += 'initializing recording clip\n'
            return_string = 'sending most recent clip\n'
            return return_string
    else:
        return_string = f'error command not recognized: {primary_command}'
        return return_string

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print('starting socket on', host, port)
    while True:
        print('awaiting client')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                data_decoded = data.decode()
                print('received', data_decoded)
                command_response = handle_command(data_decoded)
                conn.sendall(command_response.encode())

    
