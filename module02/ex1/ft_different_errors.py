def garden_operations(error):
	if error is ValueError:
		x = int("abc")
		print(x)
	if error is ZeroDivisionError:
		x = 1 / 0
		print(x)
	if error is FileNotFoundError:
		x = open(error)
		print(x)
	if error is KeyError:
		x = {'name': 'henk','house': 'brian'}
		print(x['john'])

def test_error_types():
	print("testing ValueError...")
	try:
		garden_operations(ValueError)
	except ValueError:
		print("Caught ValueError: invalid literal for int()\n")
	print("testing ZeroDivisionError...")
	try:
		garden_operations(ZeroDivisionError)
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero\n")
	print("testing FileNotFoundError...")
	try:
		garden_operations("missing.txt")
	except:
		print("Caught FileNotFoundError: No such file 'missing.txt'\n")
	print("testing KeyError...")
	try:
		garden_operations(KeyError)
	except KeyError:
		print("Caught KeyError: 'john'\n")
	print("Testing multiple errors together...")
	try:
		garden_operations(KeyError)
		garden_operations(ValueError)
	except Exception:
		print("Caught an error, but program continues!\n")
	print("All error types tested successfully!")

test_error_types()