from twophasecommit.models.slave_states import SlaveStates


class SlaveCorePayload(BaseMachine):
    state_module_map = {
        SlaveStates.INITIAL.value: 1,
        SlaveStates.WRITE_CHANGE_TO_VARIABLE.value: 1,
        SlaveStates.SEND_VOTE.value: 1,
        SlaveStates.RECEIVE_COMMIT_ABORT_MESSAGE.value: 1,
        SlaveStates.PROCESS_COMMIT_OR_ABORT.value: 1,
        SlaveStates.SUCCESS.value: 1,
        SlaveStates.ERROR.value: 1,
        SlaveStates.SEND_RESPONSE.value: 1,
    }

    def __init__(*args, **kwargs):
        super(MasterCorePayload, self).__init__(*args, **kwargs)
