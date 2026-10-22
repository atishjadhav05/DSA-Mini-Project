from collections import deque


def schedule_jobs(jobs, dependencies):
    """Generate a valid job order or report an error."""

    if len(set(jobs)) != len(jobs):
        raise ValueError("Job names must be unique.")

    job_set = set(jobs)
    graph = {job: [] for job in jobs}
    indegree = {job: 0 for job in jobs}

    # Build the adjacency list and calculate in-degrees.
    for before, after in dependencies:
        if before not in job_set or after not in job_set:
            raise ValueError(
                f"Unknown job in dependency: {before} -> {after}"
            )

        if before == after:
            raise ValueError("A job cannot depend on itself.")

        graph[before].append(after)
        indegree[after] += 1

    print("\nADJACENCY LIST")
    for job in jobs:
        print(f"{job}: {graph[job]}")

    print("\nINITIAL IN-DEGREES")
    for job in jobs:
        print(f"{job}: {indegree[job]}")

    # Queue all jobs that have no prerequisites.
    ready = deque(
        job for job in jobs if indegree[job] == 0
    )
    order = []

    print("\nSCHEDULING PROCESS")

    while ready:
        current = ready.popleft()
        order.append(current)

        print(f"\nSelected job: {current}")
        print(f"Current schedule: {order}")

        for neighbour in graph[current]:
            indegree[neighbour] -= 1

            print(
                f"Updated in-degree of {neighbour}: "
                f"{indegree[neighbour]}"
            )

            if indegree[neighbour] == 0:
                ready.append(neighbour)
                print(f"{neighbour} is now ready.")

    # If jobs remain, a dependency cycle exists.
    if len(order) != len(jobs):
        remaining = [
            job for job in jobs if indegree[job] > 0
        ]
        raise ValueError(
            f"Cycle detected. Unscheduled jobs: {remaining}"
        )

    return order


def main():
    jobs = ["A", "B", "C", "D", "E"]

    # A must finish before B, and so on.
    dependencies = [
        ("A", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E")
    ]

    print("=" * 45)
    print("       JOB SCHEDULING USING GRAPHS")
    print("=" * 45)

    print("\nJOBS")
    print(", ".join(jobs))

    print("\nDEPENDENCIES")
    for before, after in dependencies:
        print(f"{before} -> {after}")

    try:
        order = schedule_jobs(jobs, dependencies)

        print("\n" + "=" * 45)
        print("           FINAL JOB SCHEDULE")
        print("=" * 45)

        for position, job in enumerate(order, start=1):
            print(f"Step {position}: Execute Job {job}")

        print("\nValid schedule:", " -> ".join(order))
        print("Status: All jobs scheduled successfully.")

    except ValueError as error:
        print("\nSCHEDULING ERROR:", error)


if __name__ == "__main__":
    main()
