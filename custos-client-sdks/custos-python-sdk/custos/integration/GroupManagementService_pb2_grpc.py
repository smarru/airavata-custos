# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import custos.core.IamAdminService_pb2 as IamAdminService__pb2


class GroupManagementServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createGroups = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/createGroups',
        request_serializer=IamAdminService__pb2.GroupsRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.GroupsResponse.FromString,
        )
    self.updateGroup = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/updateGroup',
        request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.GroupRepresentation.FromString,
        )
    self.deleteGroup = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/deleteGroup',
        request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
        )
    self.findGroup = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/findGroup',
        request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.GroupRepresentation.FromString,
        )
    self.getAllGroups = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/getAllGroups',
        request_serializer=IamAdminService__pb2.GroupRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.GroupsResponse.FromString,
        )
    self.addUserToGroup = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/addUserToGroup',
        request_serializer=IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
        )
    self.removeUserFromGroup = channel.unary_unary(
        '/org.apache.custos.group.management.service.GroupManagementService/removeUserFromGroup',
        request_serializer=IamAdminService__pb2.UserGroupMappingRequest.SerializeToString,
        response_deserializer=IamAdminService__pb2.OperationStatus.FromString,
        )


class GroupManagementServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def createGroups(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAllGroups(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addUserToGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeUserFromGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GroupManagementServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createGroups': grpc.unary_unary_rpc_method_handler(
          servicer.createGroups,
          request_deserializer=IamAdminService__pb2.GroupsRequest.FromString,
          response_serializer=IamAdminService__pb2.GroupsResponse.SerializeToString,
      ),
      'updateGroup': grpc.unary_unary_rpc_method_handler(
          servicer.updateGroup,
          request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
          response_serializer=IamAdminService__pb2.GroupRepresentation.SerializeToString,
      ),
      'deleteGroup': grpc.unary_unary_rpc_method_handler(
          servicer.deleteGroup,
          request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
          response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
      ),
      'findGroup': grpc.unary_unary_rpc_method_handler(
          servicer.findGroup,
          request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
          response_serializer=IamAdminService__pb2.GroupRepresentation.SerializeToString,
      ),
      'getAllGroups': grpc.unary_unary_rpc_method_handler(
          servicer.getAllGroups,
          request_deserializer=IamAdminService__pb2.GroupRequest.FromString,
          response_serializer=IamAdminService__pb2.GroupsResponse.SerializeToString,
      ),
      'addUserToGroup': grpc.unary_unary_rpc_method_handler(
          servicer.addUserToGroup,
          request_deserializer=IamAdminService__pb2.UserGroupMappingRequest.FromString,
          response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
      ),
      'removeUserFromGroup': grpc.unary_unary_rpc_method_handler(
          servicer.removeUserFromGroup,
          request_deserializer=IamAdminService__pb2.UserGroupMappingRequest.FromString,
          response_serializer=IamAdminService__pb2.OperationStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.apache.custos.group.management.service.GroupManagementService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))