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
     # conditional movement
     # if we see that all the slaves gave votes then only move to next phase,
     # if we don't see votes from all the slaves, then return an error to client
     # and send a roll back message
     # If due to some issue the slaves didn't get the roll back but got request
     # for new changes then they need to understand the missing abort statemnt
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
     # If we see one of the slave is not accepting the connection or the client 
     # asked us to query a machine which no longer exists then error out
    {'trigger': 'error', 'source': MasterStates.SEND_MESSAGES_TO_SLAVES.value,
     'dest': MasterStates.ERROR.value},
     # shouldn't occur as we're handling the case of not receiving the response 
     # from slaves in the main logic
    {'trigger': 'error', 'source': MasterStates.WAIT_AND_AGGREGATE_VOTES.value,
     'dest': MasterStates.ERROR.value},
    # This doens't involve any network calls, ideally shouldn't occur
    {'trigger': 'error', 'source':
        MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value,
     'dest': MasterStates.ERROR.value},
     # If one of the slave machines goes down and the connection is lost, then throw error
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

class MasterCoreMachine():

    def __init__(self):
        state_machine = Machine(
            states=states,
            transitions=transition_actions,
            initial='initial'
        )
        self.machine = MasterCorePayload(state_machine)




