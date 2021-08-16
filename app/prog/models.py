class ProgAlgo:
    def __init__(self, algo_name="", route_name="", steps=()):
        self.algo_name = algo_name
        self.route_name = route_name
        self.steps = steps

    def json(self):
        return {
            "algo-name": self.algo_name,
            "steps": self.steps,
        }


class ProgSort:
    def __init__(self, inp=()):
        self.inp = inp
        self.result = []
        self.time_taken = 0

    def json(self):
        return {
            "arr": " ".join(map(str, self.inp)),
            "result": " ".join(map(str, self.result)),
            "time_taken": f"{self.time_taken} milliseconds",
        }
