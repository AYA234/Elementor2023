from aws_consumers import _consumer2
d = _consumer2()
d.set_topic('kamatech_order')
d.read_orders()