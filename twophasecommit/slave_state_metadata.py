from transitions import Machine
from models.slave_states import SlaveStates

states = [
    SlaveStates.INITIAL.value,
    SlaveStates.WRITE_CHANGE_TO_VARIABLE.value,
    SlaveStates.SEND_VOTE.value,
    SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
    SlaveStates.LEADER_ELECTION.value,
    SlaveStates.GET_SYNC_WITH_MASTER_DB_IF_CHOOSEN_AS_MASTER.value,
    SlaveStates.SUCCESS.value,
    SlaveStates.ERROR.value,
    SlaveStates.SEND_RESPONSE.value,
]
transition_actions = [
    # Successes
    {'trigger': 'next', 'source': SlaveStates.INITIAL.value,
     'dest': SlaveStates.WRITE_CHANGE_TO_VARIABLE.value},
    {'trigger': 'next', 'source': SlaveStates.WRITE_CHANGE_TO_VARIABLE.value,
     'dest': SlaveStates.SEND_VOTE.value},
    {'trigger': 'next', 'source': SlaveStates.SEND_VOTE.value,
     'dest': SlaveStates.PROCESS_COMMIT_OR_ABORT.value},
    {'trigger': 'next', 'source': SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
     'dest': SlaveStates.SEND_RESPONSE.value},

    {'trigger': 'next', 'source':
        SlaveStates.GET_SYNC_WITH_MASTER_DB_IF_CHOOSEN_AS_MASTER.value,
     'dest': SlaveStates.SUCCESS.value},
    {'trigger': 'next', 'source': SlaveStates.SUCCESS.value,
     'dest': SlaveStates.SUCCESS.value},
    {'trigger': 'next', 'source': SlaveStates.ERROR.value,
     'dest': SlaveStates.SUCCESS.value},
    {'trigger': 'next', 'source': SlaveStates.SEND_RESPONSE.value,
     'dest': SlaveStates.SUCCESS.value},
    # Election
    {'trigger': 'election', 'source': '*', 'dest': SlaveStates.LEADER_ELECTION.value},
    # Failures
    {'trigger': 'error', 'source': SlaveStates.INITIAL.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source': SlaveStates.WRITE_CHANGE_TO_VARIABLE.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source': SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source': SlaveStates.LEADER_ELECTION.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source':
        SlaveStates.GET_SYNC_WITH_MASTER_DB_IF_CHOOSEN_AS_MASTER.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source': SlaveStates.SUCCESS.value,
     'dest': SlaveStates.SUCCESS.value},
    {'trigger': 'error', 'source': SlaveStates.ERROR.value,
     'dest': SlaveStates.ERROR.value},
    {'trigger': 'error', 'source': SlaveStates.SEND_RESPONSE.value,
     'dest': SlaveStates.ERROR.value},

    # Default State from success in initial
    {'trigger': '*', 'source':
        SlaveStates.SUCCESS.value, 'dest': SlaveStates.SEND_RESPONSE.value},

    # Default State from error in initial
    {'trigger': '*', 'source':
        SlaveStates.ERROR.value, 'dest': SlaveStates.SEND_RESPONSE.value},

    {'trigger': '*', 'source':
        SlaveStates.SEND_RESPONSE.value, 'dest': SlaveStates.INITIAL.value},
]

machine = Machine(
    states=states,
    transitions=transition_actions,
    initial='initial'
)
