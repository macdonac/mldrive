import setuptools
setuptools.setup(
    name= "mldrive",
    version="0.2.1",
    author="mldrive",
    description='A Python wrapper for the MLdrive API. Functionality includes getting datasets, saving dataframes/models, loading dataframes/models, sending dataframes/models, recieving dataframes/models.',
  install_requires=[            
          'pandas',
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)