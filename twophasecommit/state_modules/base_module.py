class BaseStateModule(object):

	def handler(self, machine, *args, **kwargs):
		# machine.next/machin.error
		raise NotImplementedError();
