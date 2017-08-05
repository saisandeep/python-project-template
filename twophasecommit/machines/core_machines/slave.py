from transitions import Machine
from models.slave_states import SlaveStates

states = [
    SlaveStates.INITIAL.value,
    SlaveStates.WRITE_CHANGE_TO_VARIABLE.value,
    SlaveStates.SEND_VOTE.value,
    SlaveStates.RECEIVE_COMMIT_ABORT_MESSAGE.value,
    SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
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
     'dest': SlaveStates.RECEIVE_COMMIT_ABORT_MESSAGE.value},
    {'trigger': 'next', 'source': SlaveStates.RECEIVE_COMMIT_ABORT_MESSAGE.value,
     'dest': SlaveStates.PROCESS_COMMIT_OR_ABORT.value},
    {'trigger': 'next', 'source': SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
     'dest': SlaveStates.SUCCESS.value},
    {'trigger': 'next', 'source': SlaveStates.SUCCESS.value,
     'dest': SlaveStates.SEND_RESPONSE.value},     

    # Failures
    
    {'trigger': 'error', 'source': SlaveStates.INITIAL.value,
     'dest': SlaveStates.ERROR.value},
    # if the slave goes down, goto error state that will mostly notify the master
    # about the down status or the master can just wait until this slave timesout
    {'trigger': 'error', 'source': SlaveStates.WRITE_CHANGE_TO_VARIABLE.value,
     'dest': SlaveStates.ERROR.value},
    # if we don't find the master connection or if the master connection is closed then throw an error
    {'trigger': 'next', 'source': SlaveStates.SEND_VOTE.value,
     'dest': SlaveStates.RECEIVE_COMMIT_ABORT_MESSAGE.value},
     # if the slave goes down, goto error state that will mostly notify the master
    # about the down status or the master can just wait until this slave timesout
    {'trigger': 'error', 'source': SlaveStates.PROCESS_COMMIT_OR_ABORT.value,
     'dest': SlaveStates.ERROR.value},
    # not sure if this makes sense
    {'trigger': 'error', 'source': SlaveStates.SUCCESS.value,
     'dest': SlaveStates.ERROR.value},
    # some sort of run time exception and not an expected on
    {'trigger': 'error', 'source': SlaveStates.ERROR.value,
     'dest': SlaveStates.ERROR.value},
     # some sort of run time exception and not an expected on
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

class SlaveCoreMachine():

    def __init__(self):
        state_machine = Machine(
            states=states,
            transitions=transition_actions,
            initial='initial'
        )
        self.machine = MasterCorePayload(state_machine)

