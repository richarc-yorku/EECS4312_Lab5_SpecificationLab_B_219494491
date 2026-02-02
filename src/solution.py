## Student Name: Richard Carmichael
## Student ID: 219494491

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # Validate resources
    if not isinstance(resources, dict):
        raise ValueError("Resources must be a dictionary.")
    for r, cap in resources.items():
        if not isinstance(r, str):
            raise ValueError(f"Resource name {r} must be a string.")
        if not isinstance(cap, (int, float)):
            raise ValueError(f"Resource capacity for {r} must be a number.")
        if cap < 0:
            raise ValueError(f"Resource capacity for {r} cannot be negative.")
    
    # Validate requests
    if not isinstance(requests, list):
        raise ValueError("Requests must be a list.")
    for i, req in enumerate(requests):
        if not isinstance(req, dict):
            raise ValueError(f"Request {i} must be a dictionary.")
        for res, amount in req.items():
            if not isinstance(amount, (int, float)):
                raise ValueError(f"Request {i} for resource '{res}' must be a number.")
            if amount < 0:
                raise ValueError(f"Request {i} for resource '{res}' cannot be negative.")

    # Initialize running totals for each resource
    running_totals = {r: 0 for r in resources}

    # Iterate over all requests
    for req in requests:
        for res, amount in req.items():
            # If a requested resource is not in resources, allocation is impossible
            if res not in resources:
                return False
            running_totals[res] += amount
            # If running total exceeds capacity, return False immediately
            if running_totals[res] > resources[res]:
                return False

    # If no capacity is exceeded, allocation is feasible
    return True
