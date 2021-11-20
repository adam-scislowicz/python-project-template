cmake_minimum_required(VERSION 3.4...3.22)

set(CMAKE_PREFIX_PATH /databricks/python3/lib/python3.8/site-packages/pybind11)

# Dump environment variables
execute_process(COMMAND "${CMAKE_COMMAND}" "-E" "environment")

# Dump internal variables
get_cmake_property(_variableNames VARIABLES)
list (SORT _variableNames)
foreach (_variableName ${_variableNames})
    message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

project(gataca.native LANGUAGES C CXX)
set(CMAKE_C_STANDARD 17 CACHE STRING "C version selection")
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 20 CACHE STRING "C++ version selection")
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3 -std=c17 -Werror -D_GNU_SOURCE -g -pg")
#if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
	# clang++-12
#	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++20 -Werror -D_GNU_SOURCE -fprofile-instr-generate -fcoverage-mapping")
#elseif (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
#	if (APPLE)
#		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++20 -fconcepts -Werror -D_GNU_SOURCE -g")
#	else()
#		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++20 -fconcepts -Werror -D_GNU_SOURCE -g -pg")
		# -Wno-stringop-overflow : spdlog is triggering this warning. disabling for now.
		# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-stringop-overflow -fsanitize=address -fsanitize=undefined -fno-sanitize-recover=all -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize=null -fno-sanitize=alignment")
#	endif()
#endif()

IF(APPLE)
    set(CMAKE_THREAD_LIBS_INIT "-lpthread")
    set(CMAKE_HAVE_THREADS_LIBRARY 1)
    set(CMAKE_USE_WIN32_THREADS_INIT 0)
    set(CMAKE_USE_PTHREADS_INIT 1)
ENDIF()
set(THREADS_PREFER_PTHREAD_FLAG ON)
#find_package(Threads REQUIRED)
#find_package(spdlog REQUIRED)
#find_package(fmt REQUIRED)
#find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

#find_package(benchmark REQUIRED)
#set(BENCHMARK_DOWNLOAD_DEPENDENCIES ON)
#add_subdirectory(${PROJECT_DIR}/third_party/benchmark)

if (APPLE)
	set(TOOL_PREFIX xcrun)
#	set(DLIB_PREFIX
#		DYLD_LIBRARY_PATH=${PROJECT_SOURCE_DIR}/onnxruntime-bin/onnxruntime-osx-x64-1.8.0/lib)
endif()
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
	set(TOOL_PREFIX)
#	set(DLIB_PREFIX
#		LD_LIBRARY_PATH=${PROJECT_SOURCE_DIR}/onnxruntime-bin/onnxruntime-linux-x64-1.9.0/lib)
endif()

pybind11_add_module(cxxmod SHARED src/cxx/main.cpp)
#target_link_libraries(cxxmod PRIVATE Threads::Threads spdlog::spdlog fmt::fmt-header-only)
