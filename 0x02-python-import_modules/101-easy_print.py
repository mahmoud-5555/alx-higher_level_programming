#!/usr/bin/python3
exec("try: 1/0\nexcept: __import__('os').write(1, b'#pythoniscool\\n')")
