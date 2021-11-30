#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <iostream>
#include <stdio.h>

#include "main.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

void testing(void) { printf("hello from c(xx) via pybind11\n"); }

ExampleClass::ExampleClass() { printf("ExampleClass constructor variant A\n"); }

ExampleClass::ExampleClass(pybind11::object dict) {

  printf("ExampleClass constructor variant B\n");

  for (auto item : (pybind11::dict)dict) {
    std::cout << "    key: " << item.first << ", value: " << item.second << "\n";
  }
}

void ExampleClass::OverloadedMethod() { printf("ExampleClass overloaded method variant A\n"); }

void ExampleClass::OverloadedMethod(int val_in) {
  printf("ExampleClass overloaded method variant B (val=%d)\n", val_in);
}

void ExampleClass::Method() { printf("ExampleClass method\n"); }

ExampleClass::~ExampleClass() { printf("ExampleClass destructor\n"); }

PYBIND11_MODULE(cxxmod, m) {

  m.doc() = "module documentation section";

  // simple function binding
  m.def("testing", &testing, "this is a test");

  // enum bindings
  pybind11::enum_<ExampleEnum>(m, "ExampleEnum")
      .value("kExampleEnumValOne", ExampleEnum::kExampleEnumValOne)
      .value("kExampleEnumValTwo", ExampleEnum::kExampleEnumValTwo)
      .export_values();

  pybind11::class_<ExampleClass>(m, "ExampleClass")
      .def(pybind11::init<>())
      .def(pybind11::init<pybind11::object>())
      .def("OverloadedMethod", pybind11::overload_cast<>(&ExampleClass::OverloadedMethod))
      .def("OverloadedMethod", pybind11::overload_cast<int>(&ExampleClass::OverloadedMethod))
      .def("Method", &ExampleClass::Method)
      .def_readwrite("val", &ExampleClass::val);

#ifdef VERSION_INFO
  m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
  m.attr("__version__") = "dev";
#endif
}