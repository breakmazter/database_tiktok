__all__ = ('RABBITMQ_URL', 'POSTGRES_URL', 'REDIS_URL')


# CONFIGS FOR RABBITMQ
RABBITMQ_HOST = '34.94.7.254'
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = '/'
RABBITMQ_LOGIN = 'mazan'
RABBITMQ_PASSWORD = 'mazan'

RABBITMQ_URL = f'''amqp://{RABBITMQ_LOGIN}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'''


# CONFIGS FOR REDIS
REDIS_HOST = '34.83.238.11'
REDIS_PORT = 6379
REDIS_USERNAME = 'user'
REDIS_PASSWORD = 'LYWxyNDJSg7h'

REDIS_URL = f'''redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'''

# CONFIGS FOR POSTGRES
POSTGRES_HOST = '127.0.0.1'
POSTGRES_PORT = 5432
POSTGRESS_DB = 'tik_tok'
POSTGRES_LOGIN = 'iosif'
POSTGRES_PASSWORD = 'fa22qge3'

POSTGRES_URL = f'postgresql://{POSTGRES_LOGIN}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRESS_DB}'
