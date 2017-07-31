from enum import Enum


class SlaveStates(Enum):
    INITIAL = 'initial',
    SEND_MESSAGES_TO_SLAVES = 'send_messages_to_slaves',
    WAIT_AND_AGGREGATE_VOTES = 'wait_and_aggregate_votes',
    PREPARE_COMMIT_OR_ABORT_MESSAGES = 'prepare_commit_or_abort_message',
    SEND_COMMIT_OR_ABORT_MESSAGES = 'send_commit_or_abort_message',
    SUCCESS = 'success',
    ERROR = 'error'
