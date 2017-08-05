from enum import Enum


class LeaderElectionStates(Enum):
    INITIAL = 'initial'
	SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER = 'submit_candidature_and_broadcast_chosen_master'
	SYNC_WITH_MASTER_DB = 'sync_with_master_db'
	SYNC_WITH_SLAVE_NODES = 'sync_with_slave_nodes'
	SYNC_WITH_MASTER_NODE = 'sync_with_master_node'
	SUCCESS = 'success'
	ERROR = 'error' 
	SEND_RESPONSE = 'send_response'
