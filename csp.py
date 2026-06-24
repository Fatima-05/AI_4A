from typing import Dict, List, Optional, TypeVar, Generic, Any

V=TypeVar('V')
D=TypeVar('D')

class Constraint(Generic[V,D]):
    def __init__(self,variables:List[V]):
        self.variables=variables

    def satisfied(self,assignment:Dict[V,D])->bool:
        return True


class CSP(Generic[V,D]):
    def __init__(self,variables:List[V],domains:Dict[V,List[D]]):
        self.variables=variables
        self.domains=domains
        self.constraints:Dict[V,List[Constraint[V,D]]]={v:[] for v in variables}

    def add_constraint(self,constraint:Constraint[V,D]):
        for var in constraint.variables:
            if var not in self.variables:
                raise ValueError(f"Variable {var} not in CSP")
            self.constraints[var].append(constraint)

    def is_consistent(self,var:V,assignment:Dict[V,D])->bool:
        for constraint in self.constraints[var]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,assignment:Dict[V,D]=None)->Optional[Dict[V,D]]:
        if assignment is None:
            assignment={}

        if len(assignment)==len(self.variables):
            return assignment

        unassigned=[v for v in self.variables if v not in assignment]
        var=unassigned[0]

        for value in self.domains[var]:
            assignment[var]=value
            if self.is_consistent(var,assignment):
                result=self.backtracking_search(assignment)
                if result is not None:
                    return result
            del assignment[var]

        return None