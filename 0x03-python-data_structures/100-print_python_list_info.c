#include <Python.h>

/**
 * print_python_list_info - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int l_size;
	int i;
	PyListObject *l_obj;

	l_size = PyList_Size(p);
	l_obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", l_size);
	printf("[*] Allocated = %li\n", l_obj->allocated);
	for (i = 0; i < l_size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(l_obj->ob_item[i])->tp_name);
}
