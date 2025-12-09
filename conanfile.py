from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, apply_conandata_patches
import os

class MylibConan(ConanFile):
    name = "mylib"
    version = "0.1"
    license = "MIT"
    description = "Minimal example library"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*", "CMakeLists.txt", "test_package/*"

    def source(self):
        apply_conandata_patches(self)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "*.h", src=os.path.join(self.source_folder, "src"), dst=os.path.join(self.package_folder, "include"))
        # copy binaries/libs
        copy(self, "*.lib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.so", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.dll", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"), keep_path=False)

    def package_info(self):
        # properties used by CMakeDeps / consumers
        self.cpp_info.set_property("cmake_file_name", "mylib")
        self.cpp_info.set_property("cmake_target_name", "mylib::mylib")
        self.cpp_info.libs = ["mylib"]