from enum import Enum


class MasterStates(Enum):
    INITIAL = 'initial'
    WRITE_CHANGE_TO_VARIABLE = 'write_change_to_variable'
    PROCESS_COMMIT_OR_ABORT = 'process_commit_or_abort'
    LEADER_ELECTION = 'leader_election'
    GET_SYNC_WITH_MASTER_DB_IF_CHOOSEN_AS_MASTER = \
        'get_sync_with_master_db_if_choosen_as_master'
    SUCCESS = 'success'
    ERROR = 'error'
