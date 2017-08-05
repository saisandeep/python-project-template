from transitions import Machine as TransitionsMachine
from twophasecommit.models.master_states import LeaderElectionStates


class LeaderElectionMasterPayload(BaseMachine):
    state_module_map = {
        LeaderElectionStates.INITIAL.value: 1,
		LeaderElectionStates.SUMBIT_CANDIDATURE_AND_BROADCAST_CHOOSEN_MASTER.value: 1,
		LeaderElectionStates.SYNC_WITH_MASTER_DB.value: 1,
		LeaderElectionStates.SYNC_WITH_SLAVE_NODES.value: 1,
		LeaderElectionStates.SYNC_WITH_MASTER_NODE.value: 1,
		LeaderElectionStates.SUCCESS.value: 1,
		LeaderElectionStates.ERROR.value: 1,
		LeaderElectionStates.SEND_RESPONS.value: 1,
    }

    def __init__(*args, **kwargs):
        super(MasterCorePayload, self).__init__(*args, **kwargs)
