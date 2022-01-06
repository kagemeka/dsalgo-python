import setuptools

setuptools.setup()
# import os
# import pathlib
# import typing

# import setuptools

# version = "0.1.0"


# cfd = os.path.dirname(__file__)
# cfd = os.path.abspath(cfd)


# def read_requirements(path: str) -> list[str]:
#     with open(file=path, mode="r") as f:
#         return [l.rstrip() for l in f.readlines() if not l.startswith("git+")]


# def find_extras_requirements(
#     root_dir: str,
# ) -> typing.Dict[str, list[str]]:
#     import glob
#     import os

#     return {
#         p.split(os.path.sep)[-2]: read_requirements(p)
#         for p in glob.glob(f"{root_dir}/**/requirements.txt", recursive=True)
#     }


# setuptools.setup(
#     name="dsalgo",
#     version=version,
#     description="",
#     long_description="",
#     long_description_content_type="text/markdown",
#     url="https://github.com/kagemeka/python-algorithms",
#     author="kagemeka",
#     author_email="kagemeka1@gmail.com",
#     maintainer="kagemeka",
#     maintainer_email="kagemeka1@gmail.com",
#     license="MIT",
#     classifiers=[
#         "License :: OSI Approved :: MIT License",
#         "Programming Language :: Python :: 3.8",
#         "Programming Language :: Python :: 3.9",
#         "Operating System :: POSIX :: Linux",
#     ],
#     package_dir={
#         "": "src",
#     },
#     packages=setuptools.find_packages(
#         where="./src/",
#         exclude=["*tests*"],
#     ),
#     include_package_data=True,
#     install_requires=read_requirements(f"{cfd}/requirements.txt"),
#     python_requires=(">=3.6, "),
#     extras_require=find_extras_requirements(f"{cfd}/src/"),
# )
