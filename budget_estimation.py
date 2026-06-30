import json
from typing import Dict, List, Optional


class BudgetEstimator:
    """Estimates travel budgets based on destination, duration, and preferences."""
    
    def __init__(self, destination: str, duration_days: int, travelers: int = 1):
        self.destination = destination
        self.duration_days = duration_days
        self.travelers = travelers
        self.expenses: Dict[str, float] = {}
    
    def add_accommodation(self, cost_per_night: float) -> None:
        """Add accommodation costs to the budget."""
        self.expenses['accommodation'] = cost_per_night * self.duration_days
    
    def add_transportation(self, flight_cost: float = 0, local_transport: float = 0) -> None:
        """Add transportation costs (flights and local transport)."""
        self.expenses['flights'] = flight_cost
        self.expenses['local_transport'] = local_transport * self.duration_days
    
    def add_food(self, daily_budget: float) -> None:
        """Add food and dining expenses."""
        self.expenses['food'] = daily_budget * self.duration_days
    
    def add_activities(self, activity_costs: List[float]) -> None:
        """Add costs for planned activities and attractions."""
        self.expenses['activities'] = sum(activity_costs)
    
    def add_miscellaneous(self, amount: float) -> None:
        """Add miscellaneous expenses (souvenirs, tips, etc.)."""
        self.expenses['miscellaneous'] = amount
    
    def calculate_total(self) -> float:
        """Calculate the total budget estimate."""
        total = sum(self.expenses.values())
        return total * self.travelers
    
    def get_breakdown(self) -> Dict[str, float]:
        """Get a detailed breakdown of expenses."""
        breakdown = self.expenses.copy()
        breakdown['total'] = self.calculate_total()
        breakdown['per_person'] = self.calculate_total() / self.travelers if self.travelers > 0 else 0
        return breakdown
    
    def to_json(self) -> str:
        """Export budget estimate as JSON."""
        return json.dumps(self.get_breakdown(), indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'BudgetEstimator':
        """Create a BudgetEstimator instance from JSON data."""
        data = json.loads(json_str)
        estimator = cls(
            destination=data.get('destination', 'Unknown'),
            duration_days=data.get('duration_days', 1),
            travelers=data.get('travelers', 1)
        )
        estimator.expenses = data.get('expenses', {})
        return estimator
    
    def __str__(self) -> str:
        breakdown = self.get_breakdown()
        result = f"Budget Estimate for {self.destination} ({self.duration_days} days, {self.travelers} traveler(s)):\n"
        result += "-" * 50 + "\n"
        for category, amount in self.expenses.items():
            result += f"{category.capitalize()}: ${amount:,.2f}\n"
        result += "-" * 50 + "\n"
        result += f"Total: ${breakdown['total']:,.2f}\n"
        if self.travelers > 1:
            result += f"Per Person: ${breakdown['per_person']:,.2f}\n"
        return result
