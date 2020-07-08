# snowflake.py

This is just a simple library for creating and managing twitter-like snowflake identifiers.


## How do I use it?
Its honestly really simple to generate a snowflake.

```python
import snowflake
import time

# The generator takes 3 arguments,
# The epoch timestamp, The number of seconds since the Unix Epoch
#   That we want to base all of our snowflake timestamps from.
#   By default it does time.time()/1000 and uses that.
# The process_id, By default it is the PID of the process however this can be
#   Whatever identifer you would like
# The worker_id, By default its 0, However it can also be whatever number you decide.
generator = snowflake.Generator()

# Then we just call generate and optionally provide a timestamp
snowflake = generator.generate()
```
Once you generate the snowflake, you can get an int using `int()` or string using `str()`,
It has some properties added to it, they are `timestamp`, `process_id`, and `worker_id` and they give as they say.

Its pretty simple. :)

if you have any issues or questions feel free to post an issue.