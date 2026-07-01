# Budget Estimation Module for Travel Planning
# Adapted from OSU-NLP-Group/TravelPlanner

def estimate_budget(destination, duration, travel_style='moderate'):
    """Estimate the total budget for a trip.

    Args:
        destination: The travel destination
        duration: Number of days for the trip
        travel_style: One of 'budget', 'moderate', or 'luxury'

    Returns:
        dict: Estimated costs broken down by category
    """
    base_costs = {
        'budget': {'accommodation': 50, 'food': 30, 'transport': 20, 'activities': 15},
        'moderate': {'accommodation': 120, 'food': 60, 'transport': 40, 'activities': 35},
        'luxury': {'accommodation': 300, 'food': 150, 'transport': 80, 'activities': 75}
    }

    daily_costs = base_costs.get(travel_style, base_costs['moderate'])
    total = {category: cost * duration for category, cost in daily_costs.items()}
    total['grand_total'] = sum(total.values())

    return total


def estimate_flight_cost(origin, destination, class_type='economy'):
    """Estimate flight costs between origin and destination."""
    base_prices = {
        'economy': 300,
        'business': 800,
        'first': 2000
    }
    return base_prices.get(class_type, base_prices['economy'])
