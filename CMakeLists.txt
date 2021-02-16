project(conan-test-cmake)
cmake_minimum_required(VERSION 3.1)

include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

include(${CMAKE_BINARY_DIR}/libtest-config-version.cmake)
include(${CMAKE_BINARY_DIR}/libtest-config.cmake)

include_directories(${libtest_INCLUDES_RELEASE})

### conan_basic_setup() is only used by CMake generator
### https://docs.conan.io/en/latest/reference/generators/cmake.html?highlight=conan_basic_setup
#conan_basic_setup(TARGETS)

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} libtest::libtest)

