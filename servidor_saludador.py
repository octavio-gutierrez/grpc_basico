from concurrent import futures

import grpc
import holamundo_pb2
import holamundo_pb2_grpc

class Saludador(holamundo_pb2_grpc.SaludadorServicer):

    def diHola(self, request, context):
        return holamundo_pb2.HelloReply(message="¡Hola %s!" % request.name)


def ofrece_servicios():
    puerto = "50051"    
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    holamundo_pb2_grpc.add_SaludadorServicer_to_server(Saludador(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    print("Servidor escuchando en " + puerto)
    servidor.wait_for_termination()

if __name__ == "__main__":
    ofrece_servicios()