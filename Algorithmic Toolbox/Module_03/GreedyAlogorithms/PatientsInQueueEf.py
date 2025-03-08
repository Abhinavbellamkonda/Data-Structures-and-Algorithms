def min_total_waiting_time_optimized(treatment_times):
    treatment_times.sort()
    total_waiting_time=0

    n=len(treatment_times)

    for i in range(n):
        remaining_patients = n - i - 1
        total_waiting_time += remaining_patients * treatment_times[i]
        print(f"Iteration {i+1}: Treat patient with time {treatment_times[i]} | Waiting Time: {total_waiting_time}")
    return total_waiting_time

times = [15, 20, 10]
print("Optimized Total Waiting Time:", min_total_waiting_time_optimized(times))