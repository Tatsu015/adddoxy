from setuptools import setup, find_packages

setup(
    name="adddoxy",
    version="1.0.0",
    description="Automatically add C++ doxygen comment headers to class, struct, enum, function and member variable.",
    author="s_tatsu",
    author_email="",
    packages=["."],
    py_modules=["adddoxy"],
    entry_points={"console_scripts": ["adddoxy = adddoxy:main"]},
)
