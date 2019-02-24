# signup_date, amt_points, percentage_correct, number_of_posts_weighed_in
import numpy as np
from math import pow

def user_point_counter(user, action):
    total_points = 0
    if user_logged_in_at_least_once_in_day:
        total_points += 1
    if user.action is correct_user_response and response_is_prompt:
        total_points += points_deserved_if_correct
    elif user.action is correct_user_response and not response_is_prompt:
        total_points += 0.5 * points_deserved_if_correct
    elif user.action is not correct_user_response:
        total_points -= 3 * user.points_deserved_if_correct
    else:
        total_points += 0

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

def points_deserved_if_correct(submitted_event, poster, endorser):
    if event_correct(submitted_event):
        poster.num_points += (submitted_event.num_upvotes - submitted_event.num_downvotes)
    if endorser is correct_user_response:
        endorser.num_points += pow(0.99, endorser.interaction_place)


def contribution_number(event):
    interaction_place = event.num_upvotes + event.num_downvotes + 1
    return interaction_place

def response_is_prompt(response_time, event):
    if response_time < event.time:
        return True
    else:
        return False

def correct_user_response(user_response, submitted_event):
    if event_correct(submitted_event) and user_response is upvote:
        return True
    else:
        return False

def event_correct(submitted_event):
    if submitted_event is in finally_viewable_event:
        return True
    else:
        return False

def clearly_incorrect_event(submitted_event):
    if submitted_event.num_downvotes - submitted_event.num_upvotes > 20:
        return True
    else:
        return False

def event_states(submitted_event):
    clearly_incorrect_event_list = list()
    live_events = list()
    if submitted_event is clearly_incorrect_event(submitted_event):
        clearly_incorrect_event_list.append(submitted_event)
    elif submitted_event is event_correct(submitted_event):
        list.append(submitted_event)

