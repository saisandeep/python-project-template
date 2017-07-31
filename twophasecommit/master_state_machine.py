from transitions import Machine
from twophasecommit.models.

states = [
    'initial',
    'send_messages_to_slaves',
    'wait_and_aggregate_votes',
    'prepare_commit_or_abort_message',
    'send_commit_or_abort_message',
    'success',
    'error'
]
transition_actions = [
    {''},
    {}
]

machine = Machine(
    states=states,
    transitions=transition_actions,
    initial='initial'
)
