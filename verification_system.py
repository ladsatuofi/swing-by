# signup_date, amt_points, percentage_correct, number_of_posts_weighed_in
import numpy as np
from math import pow

def segregate_student_credibility():
    # have a list of users and their points stored in string format
    list_of_users = list(** ** ** ** read from our database)
    list_of_user_points = list(** ** * read from our database)

    # turn our list of users and their points into a dictionary
    users_and_points = dict(zip(list_of_users, list_of_user_points))

    # get the top and worst users by point values
    top_users_by_points = {k: np.percentile(v, 70) for k, v in users_and_points.items()}
    bottom_users_by_points = {k: np.percentile(v, 5) for k, v in users_and_points.items()}

    # get the identities of the users who have viewed the post
    users_who_viewed_event = list(** ** * blah from Matt db ** ** * )

def voting_weightage(submitted_event):
    submitted_event.num_upvotes = 0
    for interactive_user in list_of_users:
        if interactive_user is in top_users_by_points:
            submitted_event.num_upvotes += 5
        elif interactive_user is in bottom_users_by_points:
            submitted_event.num_upvotes += 1
        else:
            submitted_event.num_upvotes += 2
    return submitted_event.num_upvotes

def whether_push_live(event):
    total_potential_points = 0
    for users in users_who_viewed_event:
        total_potential_points += users.voting_weightage
        if total_potential_points > 1000 and event.upvotes > 500:
            event.push_live()

def points_deserved_if_correct(submitted_event, contributor):
    if event_correct(submitted_event) and contributor is in submitted_event.posters:
        contributor.num_points += (submitted_event.num_upvotes - submitted_event.num_downvotes)
        points_deserved = (submitted_event.num_upvotes - submitted_event.num_downvotes)
    if contributor is correct_user_response and contributor is in submitted_event.endorsers:
        contributor.num_points += pow(0.99, contributor.contribution_number(submitted_event))
        points_deserved = pow(0.99, contributor.contribution_number(submitted_event))
    return points_deserved

