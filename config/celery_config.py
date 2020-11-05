from kombu import Exchange, Queue


class CeleryQueueConfig(object):
    ACTIVITY_QUEUE = ACTIVITY_ROUTING_KEY = 'activity'
    ACTIVITY_EXCHANGE = Exchange('activity', type='direct')

    QUEUES = (
        Queue(ACTIVITY_QUEUE, ACTIVITY_EXCHANGE, routing_key=ACTIVITY_ROUTING_KEY),
    )

    ROUTES = {
        'tasks.tasks.update_logs': {
            'queue': ACTIVITY_QUEUE,
            'exchange': ACTIVITY_EXCHANGE
        }
    }