from twisted.application import service

def makeService(config):
  print config['greeting']
  return service.MultiService()
