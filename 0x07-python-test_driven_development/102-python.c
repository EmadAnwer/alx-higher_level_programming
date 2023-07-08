#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    Py_UNICODE *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsUnicode(p);

    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", value);
}
