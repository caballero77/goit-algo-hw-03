import argparse
import os
import shutil

def get_file_type(file_name: str) -> str:
    if '.' in file_name:
        return file_name.split('.')[-1]

    return None

def create_dir(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)

def copy(from_path: str, to_path: str):
    if not os.path.exists(from_path):
        return
    try:
        if os.path.isfile(from_path):
            file = os.path.basename(from_path)
            root = os.path.dirname(from_path)
            file_type = get_file_type(file)
            
            if file_type is None:
                shutil.copy(f'{root}/{file}', f'{to_path}/{file}')
                return

            create_dir(f'{to_path}/{file_type}')
            shutil.copy(f'{root}/{file}', f'{to_path}/{file_type}/{file}')
            return
        if os.path.isdir(from_path):
            create_dir(to_path)
            for item in os.listdir(from_path):
                copy(f'{from_path}/{item}', to_path)
    except PermissionError as e:
        raise e
    except Exception:
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, default='.')
    parser.add_argument('--dist', type=str, default='./dist')
    args = parser.parse_args()
    copy(args.source, args.dist)