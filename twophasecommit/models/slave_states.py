from enum import Enum


class SlaveStates(Enum):
    INITIAL = 'initial'
    WRITE_CHANGE_TO_VARIABLE = 'write_change_to_variable'
    SEND_VOTE = 'send_vote'
    PROCESS_COMMIT_OR_ABORT = 'process_commit_or_abort'
    SUCCESS = 'success'
    ERROR = 'error'
    SEND_RESPONSE = 'send_response'
