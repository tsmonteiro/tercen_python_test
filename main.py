import sys as sys

import tercen.http.HttpClientService as tercen_http


import traceback as tb
import json

import pkg_resources
pkg_resources.require("pytson==1.0")
import pytson as ptson
import io
import urllib.request

import context as tercen

ptson.__version__


# http://127.0.0.1:5402/admin/w/7537973a65f87297878b1dd4e80015bb/ds/4523e5ce-0804-4beb-9b12-31ccd35683da
WORKFLOW_ID = '7537973a65f87297878b1dd4e80015bb'
STEP_ID = '4523e5ce-0804-4beb-9b12-31ccd35683da'

# TERCEN.COm
# https://tercen.com/tsmonteiro/w/41fcacecf20de12dea7c242117d5eeef/ds/13691224-316a-426e-ad88-937f33290ecd
# WORKFLOW_ID = '41fcacecf20de12dea7c242117d5eeef'
# STEP_ID = '13691224-316a-426e-ad88-937f33290ecd'

# client = TercenClient("http://172.42.0.42:5400/") # Tercen URI
# session = client.userService.connect('admin', 'admin')

  # def __init__(self, workflowId=None, stepId=None, taskId=None, authToken=None,
  #                 username=None, password=None, serviceUri=None):

ctx = tercen.TercenContext( workflowId=WORKFLOW_ID, stepId=STEP_ID, 
                            username='admin', password='admin',
                            serviceUri="http://172.42.0.42:5400/")

# client = TercenClient("https://tercen.com/") # Tercen URI
# session = client.userService.connect('tsmonteiro', 'NaoTemSenha1')

cubeQuery = ctx.getQuery()

cnames = []
for i, factor in enumerate(cubeQuery.colColumns):
  cnames.append(factor.name)
  
rnames = []
for i, factor in enumerate(cubeQuery.rowColumns):
  rnames.append(factor.name)

aq = cubeQuery.axisQueries[0]

print(cnames)
print(rnames)

client = ctx.getClient()

tableSchema = client.tableSchemaService.findByQueryHash( cubeQuery.qtHash)

 # findKeys = function(viewName, keys = NULL, useFactory = FALSE) {
 #        url = self$getServiceUri(self$uri, "/", viewName)
 #        body = lapply(keys, unbox)
 #        response = self$client$post(url, body = body, query = list(useFactory = tolower(toString(useFactory))))
 #        if (response$status != 200) {
 #            self$onResponseError(response, "findKeys")
 #        }
 #        list = response$content
 #        lapply(list, function(each) self$fromTson(each))
 
url = (client.tableSchemaService.getBaseUri()).resolve(tercen_http.URI.create(cubeQuery.qtHash))
response = client.httpClient.post( "http://172.42.0.42:5400/" + url.toString(), body=None, headers=dict() )
response.status


client.tableSchemaService.get( cubeQuery.relation.id  )







# #wrkflow = client.workflowService.get(WORKFLOW_ID)
# #TODO Hand-code this
# # line ~1090 tercen client base
# uri = tercen_http.URI.create("api/v1/workflow" + "/" + "getCubeQuery")
# params = {}
# params["workflowId"] = WORKFLOW_ID
# params["stepId"] = STEP_ID
# response = client.httpClient.post(
#     client.tercenURI.resolve(uri).toString(), None, ptson.encodeTSON(params)
# )
# 
# response.body().bytes()
# 
# req = urllib.request.Request(client.tercenURI.resolve(uri).toString(),
#  headers=dict(), data=ptson.encodeTSON(params), method='POST')
# Response(urllib.request.urlopen(req))
#     
# 
# if response.code() != 200:
#     data = response.body().bytes()
#     obj = ptson.decodeTSON(data)
#     
# else:
#     answer = tercen.model.base.CubeQueryBase.createFromJson(
#         decodeTSON(response.body().bytes()))
