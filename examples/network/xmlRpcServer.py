from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime

class ExampleService:
	def ping(self):
		""" Simple function to respond when called to demonstrate connectivity."""
		return True

	def now(self):
		""" Returns the server current date and time. """
		return datetime.datetime.now()

	def show_type(self, arg):
		""" ILLUSTRATE how types are passed in and out of server methods
			Accepts one argument of any type.
			Returns a tuple with string representation of the value,
			the name of the type, and the value itself.
		"""

		return (str(arg), str(type(arg)),arg)

	def raises_exception(self, msg):
		raise RuntimeError(msg)

	
	def send_back_binary(self, bin):
		data = bin.data
		print('Send back binary ({!r})'.format(data))
		response = Binary(data)
		return response


if __name__ == '__main__':
	server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
	server.register_introspection_functions()
	server.register_multicall_functions()

	server.register_instance(ExampleService())

	try:
		print('Use Control-C to exit')
		server.serve_forever()
	except KeyboardInterrupt:
		print('Exiting')


