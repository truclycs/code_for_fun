# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        emap = {e.id: e for e in employees}
        def DFS(eid):
            employee = emap[eid]
            return (employee.importance + sum(DFS(eid) for eid in employee.subordinates))
        return DFS(id)