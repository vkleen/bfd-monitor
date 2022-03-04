import logging
import asyncio

from grpc import aio

from bfdd import bfdd_pb2
from bfdd import bfdd_pb2_grpc

from . import peer

async def monitor_peer(peer_resp):
    async with aio.insecure_channel('unix:///run/bfdd/bfdd.sock') as channel:
        stub = bfdd_pb2_grpc.BfdApiStub(channel)
        async for monitor_resp in stub.MonitorPeer(bfdd_pb2.MonitorPeerRequest(uuid = peer_resp.uuid)):
            local_state = bfdd_pb2.SessionState.Name(monitor_resp.local.state)
            remote_state = bfdd_pb2.SessionState.Name(monitor_resp.remote.state)
            logging.info(f"{peer_resp.peer.name}: local {local_state}; remote {remote_state}")

            if monitor_resp.local.state == bfdd_pb2.SessionState.DOWN:
                await peer.disable(peer_resp.peer.name)
            if monitor_resp.remote.state == bfdd_pb2.SessionState.UP and monitor_resp.local.state == bfdd_pb2.SessionState.UP:
                await peer.enable(peer_resp.peer.name)
    

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
