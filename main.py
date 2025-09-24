import random


lambd = 0.99              
mu = 1 / 3.42             
K = 5                     
max_time = 100000         


clock = 0
queue = []
server_busy = False
next_arrival = random.expovariate(lambd)
next_departure = float('inf')


total_in_system_time = 0
total_in_queue_time = 0
served_customers = 0
queue_lengths = []


while clock < max_time:
    if next_arrival < next_departure:
        clock = next_arrival
        if len(queue) + int(server_busy) < K:
            queue.append(clock)
            if not server_busy:
                server_busy = True
                arrival_time = queue.pop(0)
                service_time = random.expovariate(mu)
                next_departure = clock + service_time
        next_arrival = clock + random.expovariate(lambd)
    else:
        clock = next_departure
        served_customers += 1
        time_in_system = clock - arrival_time
        total_in_system_time += time_in_system
        total_in_queue_time += arrival_time - queue[0] if queue else 0
        if queue:
            arrival_time = queue.pop(0)
            service_time = random.expovariate(mu)
            next_departure = clock + service_time
        else:
            server_busy = False
            next_departure = float('inf')
    queue_lengths.append(len(queue))


avg_time_in_system = total_in_system_time / served_customers
avg_time_in_queue = total_in_queue_time / served_customers
avg_queue_length = sum(queue_lengths) / len(queue_lengths)
utilization = served_customers * (1 / mu) / clock

print("Resultados de la simulación:")
print(f"Clientes atendidos: {served_customers}")
print(f"Tiempo promedio en el sistema: {avg_time_in_system:.4f}")
print(f"Tiempo promedio en cola: {avg_time_in_queue:.4f}")
print(f"Longitud promedio de la cola: {avg_queue_length:.4f}")
print(f"Utilización del servidor: {utilization:.4f}")