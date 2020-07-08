import time
from os import getpid
from .Snowflake import Snowflake


class Generator:
    def __init__(self, epoch=None, process_id=None, worker_id=None):
        super().__init__()
        if epoch is None:
            epoch = int(time.time() * 1000)
        if process_id is None:
            process_id = getpid()
        if worker_id is None:
            worker_id = 0

        self.epoch = epoch
        self.process_id = process_id
        self.worker_id = worker_id
        self._count = 0

    @property
    def epoch(self) -> int:
        return self._epoch

    @epoch.setter
    def epoch(self, v: int):
        self._epoch = v

    @property
    def process_id(self) -> int:
        return self._proc_id

    @process_id.setter
    def process_id(self, v: int):
        self._proc_id = v

    @property
    def worker_id(self) -> int:
        return self._work_id

    @worker_id.setter
    def worker_id(self, v: int):
        self._work_id = v

    def __repr__(self):
        return "Generator(epoch=%r,process_id=%r,worker_id=%r)" % (self.epoch, self.process_id, self.worker_id)

    def generate(self, timestamp=None) -> Snowflake:
        if timestamp is None:
            timestamp = int(time.time() * 1000)

        ep = timestamp - self.epoch

        sflake = ep << 22

        sflake |= (self.worker_id % 32) << 17
        sflake |= (self.process_id % 32) << 12
        sflake |= (self._count % 4096)

        self._count += 1

        return Snowflake(self.epoch, sflake)
