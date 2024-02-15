import grpc
import holamundo_pb2
import holamundo_pb2_grpc

def run():
    print("Intentando decir hola")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = holamundo_pb2_grpc.SaludadorStub(channel)
        respuesta = stub.diHola(holamundo_pb2.HelloRequest(name="Octavio"))
        print("El cliente recibio", respuesta.message)                         

if __name__ == "__main__":
    run()
