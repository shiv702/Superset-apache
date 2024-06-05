import os
from flask_appbuilder.security.manager import AUTH_DB  # Importing AUTH_DB

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:aqeH#$9030@database-1.cr648soospc5.us-west-2.rds.amazonaws.com:5432/supersetdb'
#SQLALCHEMY_DATABASE_URI = 'database-1.cr648soospc5.us-west-2.rds.amazonaws.com:5432/supersetdb'
WTF_CSRF_ENABLED = True
FEATURE_FLAGS = {"DASHBOARD_NATIVE_FILTERS": True}
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://superset-redis.yyrqt6.clustercfg.usw2.cache.amazonaws.com:6379/0',  # Assuming Redis is hosted at hostname 'redis'
}
LOG_LEVEL = 'DEBUG'
AUTH_TYPE = AUTH_DB
#ENABLE_PROXY_FIX = True

