from celery import Celery

class MyCelery(Celery):
    key_prefix = 'celery{mytag}:'

    def gen_task_name(self, name, module):
        # Apply a hash tag to ensure all keys related to this task map to the same slot
        return f'{self.key_prefix}{super().gen_task_name(name, module)}'

app = MyCelery('worker_app', broker='redis://superset-redis.yyrqt6.clustercfg.usw2.cache.amazonaws.com:6379/0', backend='redis://superset-redis.yyrqt6.clustercfg.usw2.cache.amazonaws.com:6379/0')

@app.task
def add(x, y):
    return x + y

