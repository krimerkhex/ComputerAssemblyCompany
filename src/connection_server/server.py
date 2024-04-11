# import fastepi
# import unicorn
# import loguru
from logger import Loger

# class FastServer(fastepi.FastAPI):
#     def __init__(self):
#         super().__init__()
#
#     def __enter__(self):
#         """Context manager entry method."""
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Context manager exit method."""
#         logger.info("Object server distracted")
#
# def start_server():
#     """Starts the front-end server for streaming video frames."""
#     try:
#         logger.add(f"Server_logs/front_server_{time_ns()}.log")
#         with FrontServer(title="No title") as server:
#             run(server, host="127.0.0.1", port=8888, log_level="info")
#     except KeyboardInterrupt:
#         logger.warning("Server stoped working")
#
#
# if __name__ == "__main__":
#     start_server()
# else:
#     logger.error("The front_server.py module cannot be run by module")

@Loger
def T(lst):
    # for i in range(len(lst)):
    #     if lst[i] < 0:
    #         lst[i] *= -1
    # return lst
    # lis[i] *= -1 if list for i in range(len(lst))
    # return lst
    return [i*(-1) if i < 0 else i for i in n]

if __name__ == "__main__":
    # app = FastServer()
    n = [i for i in range(-100000, 10000000)]
    T(n)
    # print(T(n))