
# Given a list of employee IDs and their direct managers' ID,
# find out the lowest common manager of given two employees.
# An employee can be manager of other employees.
# One employee only have one direct manager.
# E.g. {"Andy" => "Jeff", "Adam" => "Andy", "Alice" => "Adam", "Bob" => "Adam"}

      charlie
        \
        jeff
        /   \
     andy   tom <
     /          \
    adam       bob
    /   \
alice<-   bob

def lowestCommonManager(ids, emp1, emp2):#empID->mgrID
    #first, construct tree:
    """
    def mgrTree:
        self.name
        self.employees#list of employee nodes
        self.level
    """

    #then, create dictionary
    map = []
    emp->mgr
    
    level1 = emp1.level#alice level is 2| mgr 1 = jeff
    level2 = emp2.level# toms level is 2| mgr 2 = jeff
    mgr1 = map[emp1]#should return manager of emp1
    mgr2 = map[emp2]
    
    while True:<-
        if mgr1 == mgr2:
            return mgr1#jeff <-
        else:
            if level1 > level2:
                level1 -= 1
                mgr1 = map[mgr1]
            else:#level 1 < level2
                level2 -= 1
                mgr2 = map[mgr2]
          
          
          
          
    mgr1 = map[emp1]#should return manager of emp1
    mgr2 = map[emp2]
    if mgr1 == mgr2:
        return mgr1
    else:
        return None
