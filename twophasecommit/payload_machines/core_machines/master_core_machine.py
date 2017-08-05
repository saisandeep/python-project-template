from twophasecommit.models.master_states import MasterStates


class MasterCorePayload(BaseMachine):
    state_module_map = {
        MasterStates.INITIAL.value: 1,
        MasterStates.SEND_MESSAGES_TO_SLAVES.value: 1,
        MasterStates.WAIT_AND_AGGREGATE_VOTES.value: 1,
        MasterStates.PREPARE_COMMIT_OR_ABORT_MESSAGES.value: 1,
        MasterStates.SEND_COMMIT_OR_ABORT_MESSAGES.value: 1,
        MasterStates.SUCCESS.value: 1,
        MasterStates.ERROR.value: 1,
        MasterStates.SEND_RESPONSE.value: 1,
    }

    def __init__(*args, **kwargs):
        super(MasterCorePayload, self).__init__(*args, **kwargs)
