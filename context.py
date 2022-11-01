import pandas as pd
import numpy as np

from tercen.client.factory import TercenClient

class TercenContext:
  def __init__(self, workflowId=None, stepId=None, taskId=None, authToken=None,
                  username=None, password=None, serviceUri="https://tercen.com/"):
    self.client = TercenClient("http://172.42.0.42:5400/") # Tercen URI
    self.session = self.client.userService.connect('admin', 'admin')
    
    self.cubeQuery = self.client.workflowService.getCubeQuery(
        stepId=stepId, workflowId=workflowId
    )
    
  def getQuery(self):
    return self.cubeQuery
  
  def getClient(self):
    return self.client
  
  def getSession(self):
    return self.session

    
    


