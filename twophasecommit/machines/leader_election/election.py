from transitions import Machine
from models.slave_states import LeaderElectionStates

states = [
    LeaderElectionStates.INITIAL.value,
    # the last slave to sumbit the vote will broadcast the master node details to all the other slaves
    LeaderElectionStates.SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER.value,
    # conditional on being chosen as master conditions='is_chosen_as_master'
    LeaderElectionStates.SYNC_WITH_MASTER_DB.value,
    # conditional on being chosen as master conditions='is_chosen_as_master'
    LeaderElectionStates.SYNC_WITH_SLAVE_NODES.value,
    LeaderElectionStates.SYNC_WITH_MASTER_NODE.value,
    LeaderElectionStates.SUCCESS.value,
    LeaderElectionStates.ERROR.value,
    LeaderElectionStates.SEND_RESPONSE.value
]
transition_actions = [
    {'trigger': 'next', 'source': LeaderElectionStates.INITIAL.value,
     'dest': LeaderElectionStates.SUMBIT_CANDIDATURE.value},
     {'trigger': 'next', 'source': LeaderElectionStates.SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER.value,
     'dest': LeaderElectionStates.SYNC_WITH_MASTER_DB.value, 'conditions': [is_chosen_as_master]},
     {'trigger': 'next', 'source': LeaderElectionStates.SYNC_WITH_MASTER_DB.value,
     'dest': LeaderElectionStates.SYNC_WITH_SLAVE_NODES.value},
     {'trigger': 'next', 'source': LeaderElectionStates.SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER.value,
     'dest': LeaderElectionStates.SYNC_WITH_MASTER_NODE.value, 'unless': [is_chosen_as_master]},
     {'trigger': 'next', 'source': LeaderElectionStates.SYNC_WITH_MASTER_NODE.value,
     'dest': LeaderElectionStates.SUCCESS.value},
     {'trigger': 'next', 'source': LeaderElectionStates.SYNC_WITH_SLAVE_NODES.value,
     'dest': LeaderElectionStates.SUCCESS.value},
     {'trigger': 'next', 'source': LeaderElectionStates.SUCCESS.value,
     'dest': LeaderElectionStates.SEND_RESPONSE.value, 'conditions': [is_chosen_as_master]},

    # if not able to find the config system. or if not able to reach any of the participating nodes
    {'trigger': 'error', 'source': LeaderElectionStates.SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER.value,
    'dest': LeaderElectionStates.ERROR.value},
    # if some data error or db connection error creeps in
    {'trigger': 'error', 'source': LeaderElectionStates.SYNC_WITH_MASTER_DB.value,
    'dest': LeaderElectionStates.ERROR.value},
    # slaves have some issue syncing with master node
    {'trigger': 'error', 'source': LeaderElectionStates.SYNC_WITH_MASTER_NODE.value,
    'dest': LeaderElectionStates.ERROR.value},
    # master has some connection/run time issues with connecting to slave node
    {'trigger': 'error', 'source': LeaderElectionStates.SYNC_WITH_SLAVE_NODES.value,
    'dest': LeaderElectionStates.ERROR.value},

    # if in case of error do election again
    {'trigger': 'error', 'source': LeaderElectionStates.ERROR.value,
    'dest': LeaderElectionStates.INITIAL.value}         

]

class MasterCoreMachine():

    def __init__(self):
        state_machine = Machine(
            states=states,
            transitions=transition_actions,
            initial='initial'
        )
        self.machine = LeaderElectionMasterPayload(state_machine)
