import math
import numpy as np

with open("../data/distance_epicenter_aristas.txt", "r") as f:
    distances = np.loadtxt(f, dtype={'names': ('arista_id', 'distancia'), 'formats': (int, float)}, delimiter=',')

print(distances)

def calc_error_prob(distancia, max_d, max_error=1.0):
    min_d = 300
    if distancia < min_d:
        return 1.0
    
    sigma = max_d / 3.0 # 3 Adjust the standard deviation as needed
    exp = -0.5 * ((distancia / sigma) ** 2)
    prob = max_error * math.exp(exp)

    return max(0.0, min(max_error,  prob))

def calc_error_prob_all(distances, max_d, max_error=1.0):
    error_prob_all = {}
    for arista_id, distancia in distances:
        prob = calc_error_prob(distancia, max_d, max_error)
        error_prob_all[arista_id] = prob

    return error_prob_all

def main():
    max_d = 1000
    max_error = 1.0
    error_prob_all = calc_error_prob_all(distances, max_d, max_error)

    sum = 0.0
    for arista_id, prob in error_prob_all.items():
        print(f"Arista {arista_id} tiene una probabilidad de error de {prob}")
        sum += prob

    avg = sum / len(error_prob_all)

    print("Promedio de probabilidad de error de todos los enlaces: ", avg)

    with open("../sql/backup.sql", "w") as f:
        f.write("BEGIN;\n")
        for arista_id, prob in error_prob_all.items():
            f.write(f"UPDATE fibra_optica_detectada SET error_prob = {prob} WHERE gid = {arista_id};\n")
        f.write("COMMIT;\n")
            
if __name__ == "__main__":
    main()


