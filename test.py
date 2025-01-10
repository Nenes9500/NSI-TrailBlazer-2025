import time

start_time = time.perf_counter()

# Votre code se trouve ici

end_time = time.perf_counter()
execution_time = end_time - start_time
while True:
    print(f"{start_time: .5f} secondes")
