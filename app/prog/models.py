class ProgAlgoTheory:
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
    def __init__(self, inp=(), algo="", err=False):
        self.inp = inp
        self.result = []
        self.time_taken = 0
        self.algo = algo
        self.err = err

    def json(self):
        if self.err:
            return {
                "algorithm": self.algo,
                "arr": " ".join(map(str, self.inp)),
                "error": self.err,
            }
        return {
            "algorithm": self.algo,
            "arr": " ".join(map(str, self.inp)),
            "result": " ".join(map(str, self.result)),
            "time_taken": f"{self.time_taken} milliseconds",
        }


class ProgSearch:
    def __init__(self, inp=(), key=None, algo=""):
        self.inp = inp
        self.algo = algo
        self.result = -1
        self.key = key
        self.time_taken = 0
        self.comparisons = 0

    def json(self):
        t = {
            "algorithm": self.algo,
            "arr": " ".join(map(str, self.inp)),
            "key": self.key,
            "found": self.result > -1,
            "time_taken": f"{self.time_taken} milliseconds",
            "comparisons": self.comparisons,
        }
        if self.result > -1:
            t["index"] = self.result
        return t


class ProgAlgo:
    def __init__(self):
        pass
