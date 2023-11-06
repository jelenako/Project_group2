#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* hash_password(const char* password) {
    const char* key = "thisisthekey";
    size_t length_of_password = strlen(password);
    size_t length_of_key = strlen(key);

    char* hashed_password = (char*)malloc(length_of_password + 1);

    for (size_t i = 0; i < length_of_password; i++) {
        char password_char = password[i];
        char key_char = key[i];
        char result_char = password_char ^ key_char;
        hashed_password[i] = result_char;
    }

    hashed_password[length_of_password] = '\0';
    return hashed_password;
}

int check_password(const char* hash, const char* password) {
    char* calculated_hash = hash_password(password);

    int is_matched = strcmp(hash, calculated_hash) == 0;

    free(calculated_hash);

    return is_matched;
}

// prototyps

static PyObject* py_hash_password(PyObject* self, PyObject* args);
static PyObject* py_check_password(PyObject* self, PyObject* args);

static PyMethodDef hash_module_methods[] = {
    {"hash_password", py_hash_password, METH_VARARGS, "Hash a password"},
    {"check_password", py_check_password, METH_VARARGS, "Check a password"},
    {NULL, NULL, 0, NULL}
};

// Python modul
static struct PyModuleDef pythonhashmodule = {
    PyModuleDef_HEAD_INIT,
    "pythonhashmodule",
    "Python ekstenzija za hashiranje lozinke",
    -1,
    hash_module_methods
};

static PyObject* py_hash_password(PyObject* self, PyObject* args) {
    const char* password;
    if (!PyArg_ParseTuple(args, "s", &password)) {
        return NULL;
    }
    char* hashed_password = hash_password(password);
    PyObject* result = Py_BuildValue("s", hashed_password);
    free(hashed_password);
    return result;
}

static PyObject* py_check_password(PyObject* self, PyObject* args) {
    const char* hashed_password;
    const char* input_password;
    
    if (!PyArg_ParseTuple(args, "ss", &hashed_password, &input_password)) {
        return NULL;
    }

    int is_matched = check_password(hashed_password, input_password);

    if (is_matched) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

// Init python modul
PyMODINIT_FUNC PyInit_pythonhashmodule(void) {
    return PyModule_Create(&pythonhashmodule);
}
