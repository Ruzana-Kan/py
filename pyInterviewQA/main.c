// myprogram.c
#include <Python.h>

int main() {
  
    Py_Initialize();

    PyObject *pModule = PyImport_ImportModule("mymodule");

    if (pModule != NULL) {
// Get a reference to the function
        PyObject *pFunc = PyObject_GetAttrString(pModule, "add_numbers");

        if (pFunc != NULL && PyCallable_Check(pFunc)) {
            PyObject *pArgs = PyTuple_Pack(2, PyLong_FromLong(3), PyLong_FromLong(4));
            PyObject *pValue = PyObject_CallObject(pFunc, pArgs);

            if (pValue != NULL) {
                // Print the result
                printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                Py_DECREF(pValue);
            } else {
                PyErr_Print();
            }

            Py_DECREF(pArgs);
            Py_DECREF(pFunc);
        } else {
            PyErr_Print();
        }

        Py_DECREF(pModule);
    } else {
        PyErr_Print();
    }

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}

