class Snowflake(object):
    """A simple datatype that "wraps" int for handling snowflake values"""
    _flake: int
    epoch: int

    def __init__(self, epoch, flake):
        """
        Snowflake object used to handle snowflakes and get metadata from them.
        :param epoch: The time to offset the epoch with when handling timestamp related values.
        :param flake: The generated snowflake value
        """
        self._flake = flake
        self.epoch = epoch
        pass

    def __int__(self):
        return self._flake

    def __repr__(self):
        return "Snowflake(epoch=%r,flake=%r)" % (self.epoch, self._flake)

    def __str__(self):
        return str(self._flake)

    @property
    def timestamp(self) -> float:
        """
        Timestamp of snowflake creation localized to the Unix Epoch
        :return: Timestamp localized to 1970/1/1
        """
        # bits 22 and onward encode timestamp - epoch
        epochtime = self._flake >> 22

        # since the epochtime is the time *since* the epoch
        # the unix timestamp will be the time *plus* the epoch
        timestamp = epochtime + self.epoch

        # convert it back to seconds as that is how we handle other time-based values around snowflakes.
        return timestamp / 1000

    @property
    def generation(self) -> int:
        return self._flake >> 0 & 0b111111111111

    @property
    def process_id(self) -> int:
        return self._flake >> 12 & 0b11111

    @property
    def worker_id(self) -> int:
        return self._flake >> 17 & 0b11111
