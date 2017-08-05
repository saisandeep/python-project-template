from transitions import Machine
from models.master_states import MasterStates

states = [
    MasterStates.INITIAL.value,
    MasterStates.SEND_MESSAGES_TO_SLAVES.value,
    MasterStates.WAIT_AND_AGGREGATE_VOTES.value,
    MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value,
    MasterStates.SEND_COMMIT_OR_ABORT_MESSAGES.value,
    MasterStates.SUCCESS.value,
    MasterStates.ERROR.value,
    MasterStates.SEND_RESPONSE.value,
]
transition_actions = [
    # Successes
    {'trigger': 'next', 'source': MasterStates.INITIAL.value,
     'dest': MasterStates.SEND_MESSAGES_TO_SLAVES.value},
    {'trigger': 'next', 'source': MasterStates.SEND_MESSAGES_TO_SLAVES.value,
     'dest': MasterStates.WAIT_AND_AGGREGATE_VOTES.value},
    {'trigger': 'next', 'source': MasterStates.WAIT_AND_AGGREGATE_VOTES.value,
     'dest': MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value},
    {'trigger': 'next', 'source':
        MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value,
     'dest': MasterStates.SEND_COMMIT_OR_ABORT_MESSAGES.value},
    {'trigger': 'next', 'source':
        MasterStates.SEND_COMMIT_OR_ABORT_MESSAGES.value,
     'dest': MasterStates.SUCCESS.value},

    # Failures
    {'trigger': 'error', 'source': MasterStates.INITIAL.value,
     'dest': MasterStates.ERROR.value},
    {'trigger': 'error', 'source': MasterStates.SEND_MESSAGES_TO_SLAVES.value,
     'dest': MasterStates.ERROR.value},
    {'trigger': 'error', 'source': MasterStates.WAIT_AND_AGGREGATE_VOTES.value,
     'dest': MasterStates.ERROR.value},
    {'trigger': 'error', 'source':
        MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value,
     'dest': MasterStates.ERROR.value},
    {'trigger': 'error', 'source':
        MasterStates.SEND_COMMIT_OR_ABORT_MESSAGES.value,
     'dest': MasterStates.ERROR.value},

    # Default State from success in initial
    {'trigger': '*', 'source':
        MasterStates.SUCCESS.value, 'dest': MasterStates.SEND_RESPONSE.value},

    # Default State from error in initial
    {'trigger': '*', 'source':
        MasterStates.ERROR.value, 'dest': MasterStates.SEND_RESPONSE.value},

    {'trigger': '*', 'source':
        MasterStates.SEND_RESPONSE.value, 'dest': MasterStates.INITIAL.value},
]

machine = Machine(
    states=states,
    transitions=transition_actions,
    initial='initial'
)
