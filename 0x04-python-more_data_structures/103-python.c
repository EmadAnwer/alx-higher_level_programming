#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
/**
 * print_python_bytes - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i;
	char *bytes_str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %ld bytes:", size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %.2x", bytes_str[i] & 0xFF);
	}
	printf("\n");
}
