# Production check
import os
DEBUG = True
if 'DYNO' in os.environ:
    DEBUG = False