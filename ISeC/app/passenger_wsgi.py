import sys

import os

os.environ["OMP_NUM_THREADS"] = "4"
os.environ["OPENBLAS_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "6"
os.environ["VECLIB_MAXIMUM_THREADS"] = "4"
os.environ["NUMEXPR_NUM_THREADS"] = "6"

# replaced by deploy script
os.environ["MYSQL_DATABASE_USER"] = "MYSQL_DATABASE_USER_PLACEHOLDER"
os.environ["MYSQL_DATABASE_PASSWORD"] = "MYSQL_DATABASE_PASSWORD_PLACEHOLDER"
os.environ["MYSQL_DATABASE_DB"] = "MYSQL_DATABASE_DB_PLACEHOLDER"
os.environ["MYSQL_DATABASE_HOST"] = "MYSQL_DATABASE_HOST_PLACEHOLDER"
os.environ["MYSQL_DATABASE_PORT"] = "MYSQL_DATABASE_PORT_PLACEHOLDER"
os.environ["LOGFILE_PATH"] = "www/isec.smart-skills.pro/log"

INTERP = os.path.expanduser("/var/www/u0200264/data/flaskenv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from app import application