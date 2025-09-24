# Tarea_Ana-Maria-Hernandez
¡Con gusto, Ana! Aquí tienes una explicación clara y profesional para incluir en un archivo `README.md`, ideal si estás documentando tu simulación M/M/1/K en Python para un proyecto académico o técnico:

---

# README: Simulación de sistema de colas M/M/1/K en Python

##  Descripción

Este proyecto implementa una simulación básica de un sistema de colas M/M/1/K utilizando Python puro. El sistema modela llegadas de clientes según una distribución Poisson, tiempos de servicio exponenciales, un único servidor y una capacidad máxima limitada (K). El objetivo es calcular métricas clave del sistema y validar resultados teóricos mediante simulación.

---

## Parámetros del modelo

- `lambd`: tasa de llegada de clientes (clientes por unidad de tiempo)
- `mu`: tasa de servicio (inversa del tiempo promedio de servicio)
- `K`: capacidad máxima del sistema (cola + servidor)
- `max_time`: duración total de la simulación

---

## Lógica de simulación

- Los clientes llegan al sistema en tiempos generados por una distribución exponencial con parámetro `lambd`.
- Si hay espacio en el sistema (cola + servidor < K), el cliente entra.
- Si el servidor está libre, el cliente inicia servicio inmediatamente.
- Si el servidor está ocupado, el cliente espera en la cola.
- Los tiempos de servicio también se generan con una distribución exponencial (`mu`).
- Se actualizan estadísticas globales como tiempo en sistema, tiempo en cola, utilización del servidor y longitud promedio de la cola.

---

## Métricas calculadas

Al finalizar la simulación, se imprimen:

- `Clientes atendidos`: número total de clientes que completaron servicio
- `Tiempo promedio en el sistema`: desde llegada hasta salida
- `Tiempo promedio en cola`: tiempo de espera antes de ser atendido
- `Longitud promedio de la cola`: promedio de clientes en espera
- `Utilización del servidor`: proporción de tiempo que estuvo ocupado

---

## Ejecución

Solo necesitas tener Python instalado. Ejecuta el script con:

```bash
python main.py
```

No se requieren librerías externas.

---

## Extensiones posibles

- Adaptar el modelo para múltiples servidores (M/M/c/K)
- Exportar resultados a Excel o CSV
- Visualizar métricas con gráficos (usando `matplotlib`)
- Comparar con resultados teóricos calculados en paralelo

