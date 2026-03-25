"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 2: Algorithm Performance
"""

import os
import csv
import time
from Permutations import generate_permutations
from Sorter import MergeSort, QuickSort, ShakerSort, HeapSort


def run_all_sorts(n):
    """Run every sorting algorithm on every permutation of size n.
    Returns a dict keyed by algorithm name. Each value is a list
    of tuples: (input_array, comparison_count)."""
    perms = generate_permutations(n)
    total_perms = len(perms)
    print("n=" + str(n) + ": generated " + str(total_perms) + " permutations")

    #create one instance of each sorter
    algorithms = [MergeSort(), QuickSort(), ShakerSort(), HeapSort()]

    #results maps algorithm name to list of (input_array, comparisons)
    results = {}
    for algo in algorithms:
        results[algo.AlgorithmName] = []

    for idx, perm in enumerate(perms):
        #print progress every 1000 permutations so we know it is working
        if idx % 1000 == 0 and idx > 0:
            print("  processed " + str(idx) + " / " + str(total_perms))

        for algo in algorithms:
            sorted_arr = algo.sort(perm)
            comparisons = algo.get_comparison()
            results[algo.AlgorithmName].append((list(perm), comparisons))

    return results


def find_best_worst_avg(records):
    """Given a list of (input_array, comparisons) tuples, find the
    10 with fewest comparisons, 10 with most, and the average."""
    #sort by comparison count ascending
    sorted_records = sorted(records, key=lambda r: r[1])

    best_10 = sorted_records[:10]
    worst_10 = sorted_records[-10:]
    #reverse worst so the highest is first
    worst_10 = list(reversed(worst_10))

    total = sum(r[1] for r in records)
    avg = total / len(records) if len(records) > 0 else 0

    return {
        "best": best_10,
        "worst": worst_10,
        "average": avg
    }


def export_full_results(n, all_results, output_dir):
    """Write a CSV with every permutation and its comparison count
    for each algorithm."""
    filename = os.path.join(output_dir, "full_results_n" + str(n) + ".csv")
    #figure out how many permutations from the first algorithm
    first_algo = list(all_results.keys())[0]
    num_perms = len(all_results[first_algo])

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        #header row
        header = ["Permutation_Index", "Input_Array"]
        for algo_name in all_results:
            header.append(algo_name + "_Comparisons")
        writer.writerow(header)

        #one row per permutation
        for i in range(num_perms):
            row = [i + 1]
            #grab the input array from the first algorithm (same for all)
            input_arr = all_results[first_algo][i][0]
            row.append(str(input_arr))
            for algo_name in all_results:
                row.append(all_results[algo_name][i][1])
            writer.writerow(row)

    print("  Full results written to " + filename)


def export_summary(n, all_results, output_dir):
    """Write a summary CSV showing best 10, worst 10, and average
    for each algorithm at a given n value."""
    filename = os.path.join(output_dir, "summary_n" + str(n) + ".csv")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        for algo_name, records in all_results.items():
            analysis = find_best_worst_avg(records)

            #section header for this algorithm
            writer.writerow([])
            writer.writerow(["Algorithm", algo_name])
            writer.writerow(["Average Comparisons", round(analysis["average"], 2)])
            writer.writerow([])

            #BEST 10
            writer.writerow(["Best 10 (fewest comparisons)"])
            writer.writerow(["Rank", "Comparisons", "Input_Array"])
            for rank, (arr, comp) in enumerate(analysis["best"], start=1):
                writer.writerow([rank, comp, str(arr)])
            writer.writerow([])

            #WORST 10
            writer.writerow(["Worst 10 (most comparisons)"])
            writer.writerow(["Rank", "Comparisons", "Input_Array"])
            for rank, (arr, comp) in enumerate(analysis["worst"], start=1):
                writer.writerow([rank, comp, str(arr)])

    print("  Summary written to " + filename)


def print_summary(n, all_results):
    """Print a readable summary to the console."""
    print("")
    print("=" * 60)
    print("RESULTS FOR n = " + str(n))
    print("=" * 60)

    for algo_name, records in all_results.items():
        analysis = find_best_worst_avg(records)
        print("")
        print("--- " + algo_name + " ---")
        print("  Average comparisons: " + str(round(analysis["average"], 2)))
        print("  Best case:  " + str(analysis["best"][0][1])
              + " comparisons " + str(analysis["best"][0][0]))
        print("  Worst case: " + str(analysis["worst"][0][1])
              + " comparisons " + str(analysis["worst"][0][0]))


def main():
    """Entry point. Runs the full experiment for n = 4, 6, and 8."""
    #create an output directory for the CSV files
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    n_values = [4, 6, 8]

    for n in n_values:
        print("")
        print("Starting experiment for n = " + str(n) + " ...")
        start_time = time.time()

        all_results = run_all_sorts(n)

        elapsed = round(time.time() - start_time, 2)
        print("  Finished n=" + str(n) + " in " + str(elapsed) + " seconds")

        #export to CSV
        export_full_results(n, all_results, output_dir)
        export_summary(n, all_results, output_dir)

        #print to console
        print_summary(n, all_results)

    print("")
    print("All experiments complete. CSV files are in the '"
          + output_dir + "' folder.")


if __name__ == "__main__":
    main()
