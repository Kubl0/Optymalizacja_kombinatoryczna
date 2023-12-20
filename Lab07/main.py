import networkx as nx
import matplotlib.pyplot as plt


class Task:
    def __init__(self, duration, dependencies):
        self.duration = duration
        self.dependencies = dependencies
        self.earliest_start = 0
        self.earliest_finish = 0
        self.latest_start = float('inf')
        self.latest_finish = float('inf')

    def __str__(self):
        return f"ES: {self.earliest_start}, EF: {self.earliest_finish}, LS: {self.latest_start}, LF: {self.latest_finish}"


def is_acyclic(tasks):
    visited = set()
    stack = set()

    def dfs(n):
        visited.add(n)
        stack.add(n)

        for neighbor in tasks[n].dependencies:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(n)
        return False

    for node in tasks:
        if node not in visited:
            if dfs(node):
                return False

    return True


def cpm(tasks):
    graph = {index: task for index, task in enumerate(tasks)}

    if not is_acyclic(graph):
        raise Exception("Graph is not acyclic")

    calculate_earliest_times(tasks)
    calculate_latest_times(tasks)

    for task in tasks:
        print(f"{chr(ord('A') + tasks.index(task))}: {task}")

    critical_path = []
    for task in tasks:
        if task.earliest_start == task.latest_start and task.earliest_finish == task.latest_finish:
            critical_path.append(tasks.index(task))

    print(f"\nCritical path: {critical_path}")
    visualize_graph(tasks)
    gantt(tasks)


def calculate_earliest_times(tasks):
    for task in tasks:
        if len(task.dependencies) == 0:
            task.earliest_start = 0
            task.earliest_finish = task.duration
        else:
            task.earliest_start = max([tasks[dependency].earliest_finish for dependency in task.dependencies])
            task.earliest_finish = task.earliest_start + task.duration


def calculate_latest_times(tasks):
    for task in reversed(tasks):
        if tasks.index(task) == len(tasks) - 1:
            task.latest_finish = task.earliest_finish
            task.latest_start = task.latest_finish - task.duration

        depending_tasks = []
        for t in tasks:
            if tasks.index(task) in t.dependencies:
                depending_tasks.append(t)

        if len(depending_tasks) > 0:
            task.latest_finish = min([t.latest_start for t in depending_tasks])
            task.latest_start = task.latest_finish - task.duration


def gantt(tasks):
    task_names = [chr(ord('A') + index) for index in range(len(tasks))]
    task_starts = [task.earliest_start for task in tasks]
    task_durations = [task.duration for task in tasks]

    fig, ax = plt.subplots()

    ax.barh(task_names, task_durations, left=task_starts, color='skyblue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Gantt Chart - Project Schedule')

    plt.show()


def visualize_graph(tasks):
    G = nx.DiGraph()

    for index, task in enumerate(tasks):
        G.add_node(chr(ord('A') + index),
                   label=f"{chr(ord('A') + index)}\nES: {task.earliest_start}\nEF: {task.earliest_finish}\nLS: {task.latest_start}\nLF: {task.latest_finish} \n {task.duration}")

        for dependency in task.dependencies:
            G.add_edge(chr(ord('A') + dependency), chr(ord('A') + index))

    pos = nx.shell_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    node_labels = nx.get_node_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=8, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


def main():
    tasks = [
        Task(0.5, []),
        Task(1, [0]),
        Task(5, [1]),
        Task(3, [2]),
        Task(4, [1]),
        Task(3, [1]),
        Task(0.5, [2]),
        Task(0.5, [3, 4, 5]),
        Task(0.5, [6, 7]),
    ]

    cpm(tasks)


if __name__ == "__main__":
    main()
