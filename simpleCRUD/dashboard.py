"""Helper module for gathering Dashboard data."""

from models import User
from django.db.models import Count

def get_current_user(id):
    """
    Gets most recent user.

    Parameters:
    - `id` - ID of currently logged in user, provided by session.
    """

    # Retrieves current user and returns it:
    current_user = User.objects.get(id=id)
    return current_user

# More functions could go here for other data or queries needed.

def populate_data(id):
    """
    Create dictionary for Dashboard Template.

    Parameters:
    - `id` - Session user id of currently logged in user.
    """

    # Prepare data for Dashboard by running functions above, which collect the data we need:
    dashboard_data = {
        "current_user": get_current_user(id), # Returns current session user
        # more_stuff : could_go_here,
        # so_that : all_data,
        # for_dashboard : is_nice_n_neat,
    }

    # Send back dashboard data which contains most recent and popular secrets with like counts, and the logged in user:
    return dashboard_data
