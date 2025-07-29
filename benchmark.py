import subprocess
import time
import statistics

# Number of iterations to run for each test
ITERATIONS = 10

def run_terraform(function_name):
    """Run terraform apply and measure execution time."""
    times = []
    for _ in range(ITERATIONS):
        start_time = time.time()
        try:
            # Run terraform apply
            subprocess.run(
                ["terraform", "apply", "-auto-approve"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            end_time = time.time()
            times.append(end_time - start_time)
        except subprocess.CalledProcessError as e:
            print(f"Error running Terraform: {e.stderr}")
            return None
    return times

def main():
    # Ensure Terraform is initialized
    subprocess.run(["terraform", "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("Running benchmark for lookup and try functions...")

    # Run benchmark
    times = run_terraform("lookup_and_try")

    if times:
        avg_time = statistics.mean(times)
        std_dev = statistics.stdev(times) if len(times) > 1 else 0
        print(f"\nResults for combined lookup and try:")
        print(f"Average execution time: {avg_time:.4f} seconds")
        print(f"Standard deviation: {std_dev:.4f} seconds")
        print(f"Execution times: {times}")

if __name__ == "__main__":
    main()