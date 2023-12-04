#include <time.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that print the information of
 * the list
 * @p: is pointer to python opject
 * Return: no return value
*/
void print_python_list_info(PyObject *p)
{
	unsigned int it;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (it = 0; it < PyList_Size(p); it++)
	{
		PyObject *item = PyList_GetItem(p, it);

		if (item != NULL)
		{
			printf("Element %d: %s\n", it, item->ob_type->tp_name);
		}
		else
		{
			printf("Element %d: NULL\n", it);
		}
	}
}
