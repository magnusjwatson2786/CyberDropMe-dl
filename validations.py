import os, errno, sys, re
ERROR_INVALID_NAME = 123

def is_pathname_valid(pathname: str) -> bool:
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        _, pathname = os.path.splitdrive(pathname)

        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname) 
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    except TypeError as exc:
        return False
    else:
        return True

def is_path_creatable(pathname: str) -> bool:
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)

def is_path_exists_or_creatable(pathname: str) -> bool:
    try:
        return is_pathname_valid(pathname) and (
            os.path.exists(pathname) or is_path_creatable(pathname))
    except OSError:
        return False

def validateUrl(url):
    if not url.startswith("https://"):
        if not url.startswith("http://"):
            url="https://"+url   
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return (re.match(regex, str(url)))