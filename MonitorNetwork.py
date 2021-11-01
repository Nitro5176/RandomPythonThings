import speedtest as spd


def upload():
    return spd.Speedtest().upload()/1000000

def download():
    return spd.Speedtest().download()/1000000

def ping():
    pingms = spd.Speedtest().get_best_server()
    return pingms['latency']

print(upload())
print(download())
print(ping())

#
# servers = []
# # If you want to test against a specific server
# # servers = [1234]
#
# threads = None
# # If you want to use a single threaded test
# # threads = 1
# #
# # s = spd.Speedtest()
# # s.get_servers(servers)
# # s.get_best_server()
# # s.download(threads=threads)
# # s.upload(threads=threads)
# # s.results.share()
# #
# # results_dict = s.results.dict()

