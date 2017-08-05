class BaseState(object):

    def __init__(self, name, incoming_action, outgoing_action):
        self.state_name = name
        self.incoming_actions_descriptions = incoming_action
        self.outgoing_actions_descriptions = outgoing_action
        self.args_for_next_state = ()
        self.kwargs_for_next_state = {}

    def __repr__(self):
        return "<{} name: {}>".format(self.__class__.__name__, self.state_name)

    def go_to_next_state(self):
        next(*self.args_for_next_state, **self.kwargs_for_next_state)

    def run_core_logic(self, machine, *args, **kwargs):
        pass
        self.args_for_next_state = ()
        self.kwargs_for_next_state = {}
