from twisted.application import service

def makeService(config):
  return service.MultiService()
