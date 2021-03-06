import json
from typing import List

from app.config import conf


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
        self.arr = inp
        self.result = []
        self.time_taken = 0
        self.algo = algo
        self.err = err

    def json(self):
        if self.err:
            return {
                "algorithm": self.algo,
                "arr": " ".join(map(str, self.arr)),
                "error": self.err,
            }
        return {
            "algorithm": self.algo,
            "arr": " ".join(map(str, self.arr)),
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


class ReqponseItem:
    TYPE_LIST = "list/array"
    TYPE_INT = "integer"
    TYPE_FLOAT = "float/double"
    TYPE_STR = "string"
    TYPE_BOOL = "boolean"
    TYPE_MAP = "map/dict"

    def __init__(self, key: str, desc: str, types: list = None, optional: bool = False):
        self.key = key
        self.desc = desc
        self.types = types or ["any (string preferred)"]
        self.required = not optional


class ComplexityAnalysis:
    def __init__(self, best=None, average=None, worst=None):
        self.best = f"O({best})"
        self.average = f"O({average})"
        self.worst = f"O({worst})"


class Documentation:
    def __init__(
        self,
        subject: str,
        category: str,
        name: str,
        endpoint: str,
        method: str = "GET",
        args: List[ReqponseItem] = None,
        description: str = "",
        inp_body=None,
        sample_inp_body: dict = None,
        out_body: List[ReqponseItem] = None,
        sample_out_body: dict = None,
        sample_request_url: str = None,
        steps: List[str] = None,
        theory: str = None,
        py_code: str = None,
        additional_info: str = None,
        space_complexity: ComplexityAnalysis = None,
        time_complexity: ComplexityAnalysis = None,
        no_try = False
    ):
        self.subject = subject
        self.category = category
        self.name = name
        self.endpoint = endpoint
        self.method = method
        self.description = description
        self.args = args or []
        self.inp_body = inp_body or []
        self.sample_inp_body = (
            json.dumps(sample_inp_body, indent=conf.json_indent)
            if sample_inp_body
            else None
        )
        self.out_body = out_body or []
        self.sample_out_body = (
            json.dumps(sample_out_body, indent=conf.json_indent)
            if sample_out_body
            else None
        )
        self.sample_request_url = sample_request_url or endpoint
        self.category_html_id = (
            self.subject.replace(" ", "-") + "-" + self.category.replace(" ", "-")
        ).lower()
        self.doc_html_id = (
            self.subject.replace(" ", "-")
            + "-"
            + self.category.replace(" ", "-")
            + "-"
            + self.name.replace(" ", "-")
        ).lower()
        self.func_name = self.doc_html_id.replace("-", "_")
        self.steps = steps
        self.theory = theory.strip() if theory else None
        self.py_code = py_code.strip() if isinstance(py_code, str) else py_code
        self.additional_info = additional_info
        self.space_complexity = space_complexity
        self.time_complexity = time_complexity
        self.no_try = no_try


class HtmlUtil:
    @staticmethod
    def sup(b, e):
        return f"{b}<sup>{e}</sup>"

    @staticmethod
    def sub(b, e):
        return f"{b}<sub>{e}</sub>"
