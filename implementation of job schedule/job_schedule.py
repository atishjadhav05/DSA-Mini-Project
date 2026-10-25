from collections import deque


def schedule_jobs(jobs, dependencies):
    """Generate a valid job schedule or report an error."""

    # Check for duplicate job names
    if len(set(jobs)) != len(jobs):
        raise ValueError("Job names must be unique.")

    job_set = set(jobs)
    graph = {job: [] for job in jobs}
    indegree = {job: 0 for job in jobs}

    # Build the graph and count prerequisites
    for before, after in dependencies:
        if before not in job_set or after not in job_set:
            raise ValueError(
                f"Unknown job in dependency: {before} -> {after}"
            )

        graph[before].append(after)
        indegree[after] += 1

    # Add jobs with no prerequisites to the queue
    ready = deque(
        job for job in jobs if indegree[job] == 0
    )

    order = []

    # Perform topological sorting
    while ready:
        job = ready.popleft()
        order.append(job)

        for neighbour in graph[job]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                ready.append(neighbour)

    # Detect circular dependencies
    if len(order) != len(jobs):
        raise ValueError(
            "Cycle detected. A valid schedule cannot be created."
        )

    return order


def display_schedule(jobs, dependencies, order):
    """Display the schedule in a clean format."""

    border = "=" * 58

    print("\n" + border)
    print("              JOB SCHEDULING SYSTEM")
    print(border)

    print(f"Jobs         : {', '.join(jobs)}")
    print(
        "Dependencies : "
        + ", ".join(f"{a} -> {b}" for a, b in dependencies)
    )

    print("-" * 58)
    print("STATUS       : SUCCESS")
    print("MESSAGE      : Valid schedule generated")

    print("\nEXECUTION ORDER")
    print("  " + "  ->  ".join(order))

    print("\nSTEP-BY-STEP SCHEDULE")

    for step, job in enumerate(order, start=1):
        print(f"  {step}. Execute Job {job}")

    print("-" * 58)
    print(f"Total jobs scheduled: {len(order)}")
    print("Dependency check    : PASSED")
    print(border)


if __name__ == "__main__":

    jobs = ["A", "B", "C", "D", "E"]

    dependencies = [
        ("A", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E")
    ]

    try:
        result = schedule_jobs(jobs, dependencies)
        display_schedule(jobs, dependencies, result)

    except ValueError as error:
        print("\n" + "=" * 58)
        print("              JOB SCHEDULING SYSTEM")
        print("=" * 58)
        print("STATUS       : ERROR")
        print("MESSAGE      :", error)
        print("=" * 58)
