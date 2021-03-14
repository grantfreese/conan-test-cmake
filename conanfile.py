from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps


class BuildTestConan(ConanFile):
	name = "conan-test-cmake"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*"
	generator = "cmake"
	requires = ["libtest/0.0.1@aptera/sandbox"]
	build_requires = ["cmake/3.19.4"]

	def generate(self):
		tc = CMakeToolchain(self)
		tc.variables["CMAKE_SYSTEM_NAME"] = "Generic"
		tc.variables["CMAKE_SYSTEM_PROCESSOR"] = "cortex-m4"

		# disable linking stage of cmake compiler test build (required for crosscompilation)
		tc.variables["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"
		#tc.variables[""] = ""
		tc.generate()

		deps = CMakeDeps(self)
		deps.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure(source_folder="src")
		cmake.build()
