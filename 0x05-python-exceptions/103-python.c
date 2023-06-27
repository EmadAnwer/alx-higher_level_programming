#include <Python.h>
#include <stdio.h>
#include <string.h>
/**
 * print_python_bytes - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	string = PyBytes_AS_STRING(p);
	if (string != NULL)
	{
		size = strlen(string);
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", string[i]);
			i++;
		}
		printf("\n");
		setbuf(stdout, NULL);
	}
}
/**
 * print_python_list - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		setbuf(stdout, NULL);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}
}


/**
 * print_python_float - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_float(PyObject *p)
{
	double value;
	char *nf;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	nf = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", nf);
	setbuf(stdout, NULL);
}
