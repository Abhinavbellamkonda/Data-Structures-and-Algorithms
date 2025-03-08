def min_total_waiting_time_brute_force(treatment_times):
    n = len(treatement_times)
    treated = [False] * n
    total_wating_time = 0

    for i in range(n):
        min_time=float('inf')
        min_index=-1

        for j in range(n):
            if not treated[j] and treatment_times[j]<min_time[j]:
                min_time=treatment_times[j]
                min_index = j

        treated[min_index] = True
        total_waiting_time += (n - i - 1) * min_time

        return total_waiting_time


# Example Usage
times = [15, 20, 10]
print("Brute Force Total Waiting Time:", min_total_waiting_time_brute_force(times))





