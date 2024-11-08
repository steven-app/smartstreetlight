import ntplib
from time import ctime

class TimeSync:
    @staticmethod
    def sync_time(ntp_server="pool.ntp.org"):
        client = ntplib.NTPClient()
        response = client.request(ntp_server)
        return ctime(response.tx_time)
