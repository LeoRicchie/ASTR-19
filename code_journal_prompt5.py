import math

def create_sin_table():
    start_x = 0
    end_x = 2
    num_entries = 1000

    # Calculate the step size
    step_size = (end_x - start_x) / (num_entries - 1)

    print(f"{'x':<10}{'sin(x)':<15}")

    # Generate and print the sin(x) vs. x table
    for i in range(num_entries):
        x = start_x + i * step_size
        sin_x = math.sin(x)
        print(f"{x:<10.4f}{sin_x:<15.4f}")


if __name__ == "__main__":
    create_sin_table()