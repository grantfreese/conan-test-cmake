from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps


class BuildTestConan(ConanFile):
	name = "conan-test-cmake"
	version = "0.0.1"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*"
	requires = [
		"libtest/0.0.2@user/testing",
		"cmake/3.19.4"]

	def generate(self):
		tc = CMakeToolchain(self)
		tc.generate()
		deps = CMakeDeps(self)
		deps.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

