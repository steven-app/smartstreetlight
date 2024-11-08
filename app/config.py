import os
import redis

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///smart_streetlight.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
    
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    RATELIMIT_DEFAULT = '200 per day'
    RATELIMIT_STRATEGY = 'fixed-window'
