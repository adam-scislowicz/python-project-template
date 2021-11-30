#ifndef _CXXMOD_MAIN_H
#define _CXXMOD_MAIN_H

#include <pybind11/pybind11.h>

enum ExampleEnum { kExampleEnumValOne, kExampleEnumValTwo };

class ExampleClass {
public:
  ExampleClass();
  ExampleClass(pybind11::object dict);
  ~ExampleClass();

  void OverloadedMethod();
  void OverloadedMethod(int val_in);

  void Method();

  int val = 4;

private:
};

#endif