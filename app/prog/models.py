class ProgAlgo:
    def __init__(self, algo_name="", route_name="", steps=[]):
        self.algo_name = algo_name
        self.route_name = route_name
        self.steps = steps

    def route_info(self):
        return {
            "algo-name": self.algo_name,
            "steps": self.steps,
        }
