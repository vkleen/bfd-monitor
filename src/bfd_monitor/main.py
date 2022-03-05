import logging
import asyncio
from enum import Enum, auto

from grpc import aio

from bfdd import bfdd_pb2
from bfdd import bfdd_pb2_grpc

from . import peer

class PeerState(Enum):
    UP = auto()
    DOWN = auto()

def bfdToPeerState(bfd):
    if bfd == bfdd_pb2.SessionState.UP:
        return PeerState.UP
    else:
        return PeerState.DOWN

def process(peer_state, monitor_resp):
    if monitor_resp.local.state == bfdd_pb2.SessionState.DOWN:
        return (PeerState.DOWN, True)
    if (monitor_resp.local.state == bfdd_pb2.SessionState.UP and
        monitor_resp.remote.state == bfdd_pb2.SessionState.UP and
        peer_state == PeerState.DOWN):
        return (PeerState.UP, True)
    return (bfdToPeerState(monitor_resp.local.state), False)

async def monitor_peer(peer_resp):
    async with aio.insecure_channel('unix:///run/bfdd/bfdd.sock') as channel:
        stub = bfdd_pb2_grpc.BfdApiStub(channel)
        peer_state = PeerState.DOWN
        async for monitor_resp in stub.MonitorPeer(bfdd_pb2.MonitorPeerRequest(uuid = peer_resp.uuid)):
            local_state = bfdd_pb2.SessionState.Name(monitor_resp.local.state)
            remote_state = bfdd_pb2.SessionState.Name(monitor_resp.remote.state)
            logging.info(f"{peer_resp.peer.name}: local {local_state}; remote {remote_state}")

            peer_state, do_reset = process(peer_state, monitor_resp)
            if do_reset:
                await peer.reset(peer_resp.peer.name)

async def main():
    peers = list()
    async with aio.insecure_channel('unix:///run/bfdd/bfdd.sock') as channel:
        stub = bfdd_pb2_grpc.BfdApiStub(channel)
        async for peer_resp in stub.ListPeer(bfdd_pb2.ListPeerRequest()):
            peers.append(peer_resp)
    await asyncio.gather(*(monitor_peer(p) for p in peers))

def run():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
