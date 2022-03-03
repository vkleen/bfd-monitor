import logging
import asyncio

from grpc import aio

from gobgp import gobgp_pb2
from gobgp import gobgp_pb2_grpc

from google.protobuf.internal import enum_type_wrapper

GoBGPSessionState = enum_type_wrapper.EnumTypeWrapper(gobgp_pb2._PEERSTATE_SESSIONSTATE)

async def softreset(name):
    logging.info(f"Softreseting {name}")
    async with aio.insecure_channel('unix:///run/gobgpd/gobgpd.sock') as channel:
        stub = gobgp_pb2_grpc.GobgpApiStub(channel)
        addr = None 
        async for resp in stub.ListPeer(gobgp_pb2.ListPeerRequest(address = name, enableAdvertised = False)):
            addr = resp.peer.state.neighbor_address
            logging.info(f"{name}: {resp.peer.state.neighbor_address}")
        if addr is None:
            logging.error(f"{name}: Could not determine peer address")
            return
        await stub.ResetPeer(gobgp_pb2.ResetPeerRequest(
            address = addr,
            communication = "",
            soft = True,
            direction = gobgp_pb2.ResetPeerRequest.SoftResetDirection.BOTH
            ))
