class BaseMachine(object):
	state_module_map = {}

	def __init__(self, state_machine):
        this.state_machine = state_machine

    def start_process(self, *args, **kwargs):
        current_state_module = self.state_module_map[this.state_machine.state]
        current_state_module.next(self, *args, **kwargs)

    def _call_transition(transition_name, *args, **kwargs):
        next_state = getattr(self.state_machine, transition_name)()
        func = self.state_module_map[next_state]
        func(self, *args, **kwargs)

    def next(self, *args, **kwargs):
        _call_transition('next', *args, **kwargs)

    def error(self, *args, **kwargs):
        _call_transition('error', *args, **kwargs)
